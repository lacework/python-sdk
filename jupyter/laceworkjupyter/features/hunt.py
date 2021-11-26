"""Provides cloud hunting UI to construct LQL queries."""

import datetime
import ipywidgets

from laceworksdk import http_session
from laceworkjupyter import manager
from laceworkjupyter import utils as main_utils
from laceworkjupyter.features import utils

# The text displayed as the default table pick.
DEFAULT_TABLE_PICK = "pick a table"

# Since observation functions cannot pass arbitrary values
# we will need to make the LW context object global here.
lw_ctx = None


def add_filter_definition(change):
    """
    Adds filter definitions to the UI.
    """
    global lw_ctx

    if change["type"] != "change":
        return
    if change["name"] != "value":
        return

    filter_display = change.get("new", False)
    filter_owner = change.get("owner")
    filter_name = filter_owner.description

    filter_dict = {}
    table_filters = lw_ctx.get("hunt_filters")
    for table_filter in table_filters:
        if table_filter.get("parameter", "N/A") == filter_name:
            filter_dict = table_filter
            break

    if not filter_dict:
        return

    grid = lw_ctx.get("hunt_grid")
    box = grid[3, 1]
    children = list(box.children)

    layout = ipywidgets .Layout(height="auto", width="90%")
    if filter_display:
        children.append(
            ipywidgets.Text(
                value="",
                placeholder=filter_dict.get("hint", "Type Something"),
                description=filter_dict.get("parameter"),
                layout=layout,
                disabled=False
            )
        )
    else:
        new_children = []
        for child in children:
            if not isinstance(child, ipywidgets.Text):
                new_children.append(child)
                continue

            if child.description != filter_dict.get("parameter"):
                new_children.append(child)
        children = new_children

    box.children = children


def _generate_table_filters(change):
    """
    Adds all filters that belong to the chosen table.
    """
    global lw_ctx

    if change["type"] != "change":
        return
    if change["name"] != "index":
        return

    table_index = change.get("new", 0)
    # Since we added a default option, we need to decrease the index by one.
    table_index -= 1

    grid = lw_ctx.get("hunt_grid")
    box = grid[3, 1]

    if table_index == -1:
        # Default option, not a real table.
        box.children = []
        return

    tables = lw_ctx.get("hunt_tables", [])
    try:
        table_name = tables[table_index].get("name")
    except IndexError:
        raise ValueError(
            "Table with index {0:d} is not defined.".format(table_index))

    if not table_name:
        raise ValueError("Invalid table")

    checkboxes = []
    table_filters = lw_ctx.get("hunt_filters", [])
    layout = ipywidgets .Layout(height="auto", width="90%")
    for table_filter in table_filters:
        if table_name != table_filter.get("table", ""):
            continue
        checkboxes.append(
            ipywidgets.Checkbox(
                value=False,
                layout=layout,
                description=table_filter.get("parameter")))

    for checkbox in checkboxes:
        checkbox.observe(add_filter_definition)

    children = [ipywidgets.Label("Pick what filters to include:")]
    children.extend(checkboxes)
    children.append(ipywidgets.Label(
        "Add the values for each selected filter:"))
    box.children = children


def _verify_query(_unused_button):
    """Verify a LQL query."""
    global lw_ctx

    grid = lw_ctx.get("hunt_grid")
    table_box = grid[1, 1]
    table_widget = table_box.children[-1]
    value_widget = grid[3, 1]

    params = {}
    for child in value_widget.children:
        if not isinstance(child, ipywidgets.Text):
            continue
        params[child.description] = child.value

    evaluator_id, lql_query = utils.build_lql_query(
        table_widget.value, params)

    try:
        _ = lw_ctx.client.queries.validate(
            lql_query, evaluator_id=evaluator_id)
        verified = ipywidgets.Valid(
            value=True, description="LQL Verified")
        grid[5, :2] = verified
    except http_session.ApiError as err:
        verified = ipywidgets.Valid(
            value=False,
            description="Failure: {0}".format(err))
        grid[5, :] = verified

    lw_ctx.add("lql_query", lql_query)
    lw_ctx.add("lql_evaluator", evaluator_id)

    return True


def _execute_query(button):
    """
    Verify and execute a LQL query.
    """
    global lw_ctx

    if not _verify_query(button):
        return

    lql_query = lw_ctx.get("lql_query")
    lql_evaluator = lw_ctx.get("lql_evaluator")

    grid = lw_ctx.get("hunt_grid")
    start_widget = grid[2, 1]
    end_widget = grid[2, 4]

    start_time = start_widget.value
    end_time = end_widget.value

    if not (start_time and end_time):
        start_time, end_time = main_utils.parse_date_offset('LAST 2 DAYS')

        start_time, _, _ = start_time.partition('.')
        start_time = f'{start_time}Z'

        end_time, _, _ = end_time.partition('.')
        end_time = f'{end_time}Z'

    start_time = start_time.upper()
    if not start_time.endswith('Z'):
        start_time = f'{start_time}Z'

    try:
        _ = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError as err:
        raise ValueError(
            "Unable to verify the end time (remember it should be entered "
            "in the format 'YYYY-MM-DDTHH:MM:SSZ' ({0:s}) - {1}".format(
                start_time, err))

    end_time = end_time.upper()
    if not end_time.endswith('Z'):
        end_time = f'{end_time}Z'

    try:
        _ = datetime.datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError as err:
        raise ValueError(
            "Unable to verify the end time (remember it should be entered "
            "in the format 'YYYY-MM-DDTHH:MM:SSZ' ({0:s}) - {1}".format(
                start_time, err))

    arguments = {
        "StartTimeRange": start_time,
        "EndTimeRange": end_time
    }

    df = lw_ctx.client.queries.execute(
        evaluator_id=lql_evaluator, query_text=lql_query, arguments=arguments)

    lw_ctx.add("lql_results", df)
    utils.write_to_namespace('df', df)

    grid[5, 2:] = ipywidgets.Label(
        "Results stored in the variable df and in lw.ctx.get('lql_results')")


def cloud_hunt(ctx=None):
    """
    Displays a UI to build LQL queries to do threat hunting.
    """
    global lw_ctx  # To be able to pass the grid to widget functions.
    tables = utils.load_yaml_file("tables.yaml")
    table_filters = utils.load_yaml_file("filters.yaml")

    options = [DEFAULT_TABLE_PICK]
    options.extend([x.get("display_name") for x in tables])
    table_list = ipywidgets.Dropdown(
        options=options,
        value=DEFAULT_TABLE_PICK,
        description="",
        disabled=False
    )
    table_list.observe(_generate_table_filters)

    first_box = ipywidgets.HBox()
    first_box.children = (
        ipywidgets.Label("Pick a table: "), table_list)

    verify_button = ipywidgets.Button(
        value=False,
        description="Verify Query",
        disabled=False,
        tooltip="Build the LQL query and verify it",
        icon="check"
    )
    verify_button.on_click(_verify_query)

    execute_button = ipywidgets.Button(
        value=False,
        description="Execute Query",
        button_style="success",
        disabled=False,
        tooltip="Build the LQL query and execute it"
    )
    execute_button.on_click(_execute_query)

    grid = ipywidgets.GridspecLayout(6, 5, width="900px")
    grid[0, :] = ipywidgets.HTML(
        value=(
            "<div align=\"center\"><h1>Cloud Hunting</h1><i>Assistant to "
            "build LQL queries to perform threat hunting within your "
            "environment.</i><br/><br/></div>"))

    grid[1, 1:3] = first_box
    grid[2, 0] = ipywidgets.Label("Start Time:")
    grid[2, 1] = ipywidgets.Text(
        value="",
        placeholder="YYYY-MM-DDTHH:MM:SSZ",
        description="",
        disabled=False
    )
    grid[2, 3] = ipywidgets.Label("End Time:")
    grid[2, 4] = ipywidgets.Text(
        value="",
        placeholder="YYYY-MM-DDTHH:MM:SSZ",
        description="",
        disabled=False
    )
    grid[3, 1:3] = ipywidgets.VBox()
    grid[4, 1] = verify_button
    grid[4, 3] = execute_button

    ctx.add("hunt_grid", grid)
    ctx.add("hunt_tables", tables)
    ctx.add("hunt_filters", table_filters)
    lw_ctx = ctx
    display(grid)  # noqa: F821


manager.LaceworkManager.add_feature(cloud_hunt, "cloud_hunt")
