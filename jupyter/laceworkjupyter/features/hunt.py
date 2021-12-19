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


def _get_start_and_end_time(ctx):
    start_time = ctx.get("start_time")
    end_time = ctx.get("end_time")

    if not (start_time and end_time):
        start_time, end_time = main_utils.parse_date_offset('LAST 2 DAYS')

    start_time, _, _ = start_time.partition('.')
    start_time = f'{start_time}Z'

    end_time, _, _ = end_time.partition('.')
    end_time = f'{end_time}Z'

    return start_time, end_time


def _add_filter_definition(change):
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
    table_filters = lw_ctx.get_state(
        state="hunt_ui", key="hunt_filters")
    for table_filter in table_filters:
        if table_filter.get("parameter", "N/A") == filter_name:
            filter_dict = table_filter
            break

    if not filter_dict:
        return

    box = lw_ctx.get_state(state="hunt_ui", key="hunt_filter_box")
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

    box = lw_ctx.get_state(state="hunt_ui", key="hunt_filter_box")

    if table_index == -1:
        # Default option, not a real table.
        box.children = []
        return

    tables = lw_ctx.get_state(
        state="hunt_ui", key="hunt_tables", default_value=[])
    try:
        table_name = tables[table_index].get("name")
    except IndexError:
        raise ValueError(
            "Table with index {0:d} is not defined.".format(table_index))

    if not table_name:
        raise ValueError("Invalid table")

    checkboxes = []
    table_filters = lw_ctx.get_state(
        state="hunt_ui", key="hunt_filters", default_value=[])
    layout = ipywidgets.Layout(height="auto", width="90%")
    for table_filter in table_filters:
        if table_name != table_filter.get("table", ""):
            continue
        checkboxes.append(
            ipywidgets.Checkbox(
                value=False,
                layout=layout,
                description=table_filter.get("parameter")))

    for checkbox in checkboxes:
        checkbox.observe(_add_filter_definition)

    children = [ipywidgets.Label("Pick what filters to include:")]
    children.extend(checkboxes)
    children.append(ipywidgets.Label(
        "Add the values for each selected filter:"))
    box.children = children


def _verify_query(_unused_button):
    """Verify a LQL query."""
    global lw_ctx

    table_box = lw_ctx.get_state(state="hunt_ui", key="hunt_table_box")
    table_widget = table_box.children[-1]
    value_widget = lw_ctx.get_state(state="hunt_ui", key="hunt_filter_box")
    label_widget = lw_ctx.get_state(state="hunt_ui", key="hunt_label")

    params = {}
    for child in value_widget.children:
        if not isinstance(child, ipywidgets.Text):
            continue
        params[child.description] = child.value

    evaluator_id, lql_query = utils.build_lql_query(
        table_widget.value, params)

    lw_ctx.add("lql_query", lql_query)
    lw_ctx.add("lql_evaluator", evaluator_id)

    try:
        _ = lw_ctx.client.queries.validate(
            lql_query, evaluator_id=evaluator_id)
    except http_session.ApiError as err:
        label_widget.value = "Failure to verify: {0}".format(err)
        return False

    label_widget.value = "LQL Verified."
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

    start_widget = lw_ctx.get_state(state="hunt_ui", key="hunt_start_widget")
    start_time = start_widget.value

    end_widget = lw_ctx.get_state(state="hunt_ui", key="hunt_end_widget")
    end_time = end_widget.value

    if not (start_time and end_time):
        start_time, end_time = _get_start_and_end_time(lw_ctx)

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

    label_widget = lw_ctx.get_state(state="hunt_ui", key="hunt_label")
    label_widget.value = (
        f"{label_widget.value}.<br/><br/><b>Executing query...</b>")

    arguments = {
        "StartTimeRange": start_time,
        "EndTimeRange": end_time
    }

    df = lw_ctx.client.queries.execute(
        evaluator_id=lql_evaluator, query_text=lql_query, arguments=arguments)

    lw_ctx.add("lql_results", df)
    utils.write_to_namespace('df', df)

    rows_returned = df.shape[0]

    query_html = lql_query.replace("\n", "<br/>").replace(" ", "&nbsp;")
    label_widget.value = (
        f"<hr/><h2>Query Completed</h2><hr/>"
        f"Query: <br/>"
        f"<i>{query_html}</i>"
        f"<br/>Query has completed with {rows_returned} rows returned."
        f"<br/><br/>Results are stored in the variable '<b>df</b>'. The data "
        f"can also be accessed by the variable "
        f"'<b><i>lw.ctx.get(\"lql_results\")</i></b>'")


@manager.register_feature
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

    table_box = ipywidgets.HBox()
    table_box.children = (
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

    box_layout = ipywidgets.Layout(
        display='flex',
        flex_flow='column',
        align_items='stretch',
        width='900px')

    title = ipywidgets.HTML(
        value=(
            "<div align=\"center\"><h1>Cloud Hunting</h1><i>Assistant to "
            "build LQL queries to perform threat hunting within your "
            "environment.</i><br/><br/></div>"))

    start_time, end_time = _get_start_and_end_time(ctx)
    start_widget = ipywidgets.Text(
        value=start_time,
        placeholder="YYYY-MM-DDTHH:MM:SSZ",
        description="",
        disabled=False
    )
    end_widget = ipywidgets.Text(
        value=end_time,
        placeholder="YYYY-MM-DDTHH:MM:SSZ",
        description="",
        disabled=False
    )

    filter_box = ipywidgets.VBox()
    result_label = ipywidgets.HTML()

    grid = ipywidgets.Box(
        children=[
            title,
            table_box,
            ipywidgets.HBox(children=[
                ipywidgets.Label("Start Time:"),
                start_widget,
                ipywidgets.Label("End Time:"),
                end_widget]),
            filter_box,
            ipywidgets.HBox(children=(verify_button, execute_button)),
            result_label,
        ], layout=box_layout
    )

    ctx.add_state("hunt_ui", "hunt_table_box", table_box)
    ctx.add_state("hunt_ui", "hunt_start_widget", start_widget)
    ctx.add_state("hunt_ui", "hunt_end_widget", end_widget)
    ctx.add_state("hunt_ui", "hunt_filter_box", filter_box)
    ctx.add_state("hunt_ui", "hunt_label", result_label)

    ctx.add_state("hunt_ui", "hunt_tables", tables)
    ctx.add_state("hunt_ui", "hunt_filters", table_filters)
    lw_ctx = ctx

    display(grid)  # noqa: F821
