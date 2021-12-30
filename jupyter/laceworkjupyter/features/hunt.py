"""Provides cloud hunting UI to construct LQL queries."""

import datetime
import ipywidgets

from laceworksdk import http_session
from laceworkjupyter import manager
from laceworkjupyter import utils as main_utils
from laceworkjupyter.features import utils

# The text displayed as the default table pick.
DEFAULT_TABLE_PICK = "Pick a table"
DEFAULT_CUSTOM_PICK = "Build A Custom Query"

DEFAULT_FILTER_PICK = "Pick what filters to include:"

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


def _add_custom_filter_definition(change):
    """
    Adds a customer filter definition to the UI.
    """
    global lw_ctx

    if change["type"] != "change":
        return
    if change["name"] != "value":
        return

    filter_display = change.get("new", False)
    filter_owner = change.get("owner")
    filter_name = filter_owner.description
    parameter_name = filter_name.split()[0]

    box = lw_ctx.get_state(state="hunt_ui", key="hunt_filter_box")
    children = list(box.children)

    layout = ipywidgets .Layout(height="auto", width="90%")
    if filter_display:
        children.append(
            ipywidgets.Text(
                value="",
                placeholder="Type A Filter Value",
                description=parameter_name,
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

            if child.description != parameter_name:
                new_children.append(child)
        children = new_children

    box.children = children


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


def _generate_custom_table():
    """
    Adds a list of tables and associated filters.
    """
    global lw_ctx
    box = lw_ctx.get_state(state="hunt_ui", key="hunt_filter_box")
    datasources = lw_ctx.client.datasources.get()
    lw_ctx.add_state("hunt_ui", "hunt_datasources", datasources)
    lw_ctx.add_state("hunt_ui", "hunt_custom", True)

    tables = {x["description"]: x["name"] for _, x in datasources.iterrows()}
    table_list = ipywidgets.Dropdown(
        options=tables.keys(),
        description="Choose table",
        disabled=False
    )
    table_list.observe(_generate_custom_filters)

    children = [
        ipywidgets.Label("Available Tables to Query From:"),
        table_list
    ]
    box.children = children


def _generate_custom_filters(change):
    """
    Adds all filters that belong to a custom table.
    """
    global lw_ctx

    if change["type"] != "change":
        return
    if change["name"] != "index":
        return

    box = lw_ctx.get_state(state="hunt_ui", key="hunt_filter_box")
    datasources = lw_ctx.get_state("hunt_ui", key="hunt_datasources")
    table_index = change.get("new", 0)

    try:
        datasource = datasources.iloc[table_index]
    except IndexError:
        raise ValueError(
            "Table with index {0:d} is not defined.".format(table_index))

    table_name = datasource['name']
    table_schema = lw_ctx.client.datasources.get_datasource_schema(table_name)
    lw_ctx.add_state("hunt_ui", "hunt_custom_table_schema", table_schema)
    lw_ctx.add_state("hunt_ui", "hunt_custom_table_name", table_name)

    checkboxes = []
    return_fields = []

    layout = ipywidgets.Layout(height="auto", width="90%")
    for _, row in table_schema.iterrows():
        name = row["name"]
        return_fields.append(name)
        data_type = row["dataType"]
        description = row["description"]

        checkboxes.append(
            ipywidgets.Checkbox(
                value=False,
                layout=layout,
                description=f"{name} [{data_type}] - {description}"))

    lw_ctx.add_state("hunt_ui", "hunt_custom_return_fields", return_fields)

    for checkbox in checkboxes:
        checkbox.observe(_add_custom_filter_definition)

    children = list(box.children)
    for index, child in enumerate(children):
        if isinstance(child, ipywidgets.Label):
            if child.value == DEFAULT_FILTER_PICK:
                children = children[:index]
                break

    children.append(ipywidgets.Label(DEFAULT_FILTER_PICK))
    children.extend(checkboxes)
    children.append(ipywidgets.Label(
        "Add the values for each selected filter:"))
    box.children = children


def _generate_table_filters(change):  # noqa: C901
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

    if table_index == len(tables):
        _generate_custom_table()
        return

    # We now know we are not doing a custom table.
    lw_ctx.add_state("hunt_ui", "hunt_custom", False)

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
        if table_name not in table_filter.get("tables", []):
            continue
        checkboxes.append(
            ipywidgets.Checkbox(
                value=False,
                layout=layout,
                description=table_filter.get("parameter")))

    for checkbox in checkboxes:
        checkbox.observe(_add_filter_definition)

    children = [ipywidgets.Label(DEFAULT_FILTER_PICK)]
    children.extend(checkboxes)
    children.append(ipywidgets.Label(
        "Add the values for each selected filter:"))
    box.children = children


def _build_standard_query():
    """
    Returns a tuple with an evaluator ID and a LQL query from definitions.
    """
    global lw_ctx

    table_box = lw_ctx.get_state(state="hunt_ui", key="hunt_table_box")
    table_widget = table_box.children[-1]
    value_widget = lw_ctx.get_state(state="hunt_ui", key="hunt_filter_box")

    params = {}
    for child in value_widget.children:
        if not isinstance(child, ipywidgets.Text):
            continue
        params[child.description] = child.value

    query_dict = utils.get_query_definition(
        table_widget.value, params)
    query_name = query_dict.get("table_name", "No Table").replace(" ", "_")
    evaluator_id = query_dict.get("evaluator_id")

    lql_query = utils.build_lql_query(query_name, query_dict)

    return evaluator_id, lql_query


def _build_custom_query():
    """
    Returns a tuple with an evaluator ID and a LQL from a custom definitions.
    """
    global lw_ctx

    value_widget = lw_ctx.get_state(state="hunt_ui", key="hunt_filter_box")
    table_schema = lw_ctx.get_state(
        state="hunt_ui", key="hunt_custom_table_schema")

    filters = []
    for child in value_widget.children:
        if not isinstance(child, ipywidgets.Text):
            continue
        attribute = child.description
        attribute_series = table_schema[
            table_schema.name == attribute].iloc[0]
        attribute_type = attribute_series['dataType']

        if attribute_type == 'String':
            filters.append(utils.format_generic_string(
                attribute=attribute, event_value=child.value))
        else:
            # TODO: Add more handling here.
            filters.append("{attribute} == {child.value}")

    query_dict = {
        "table_name": lw_ctx.get_state(
            state="hunt_ui", key="hunt_custom_table_name"),
        "filters": filters,
        "return_fields": lw_ctx.get_state(
            state="hunt_ui", key="hunt_custom_return_fields"),
    }

    lql_query = utils.build_lql_query(
        "CustomQueryBuild", query_dict)

    if query_dict.get("table_name", "") == "CloudTrailRawEvents":
        evaluator_id = "Cloudtrail"
    else:
        evaluator_id = None

    return evaluator_id, lql_query


def _verify_query(_unused_button):
    """
    Verify a LQL query.
    """
    global lw_ctx

    label_widget = lw_ctx.get_state(state="hunt_ui", key="hunt_label")

    custom_query = lw_ctx.get_state("hunt_ui", key="hunt_custom")
    if custom_query:
        evaluator_id, lql_query = _build_custom_query()
    else:
        evaluator_id, lql_query = _build_standard_query()

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
    options.append(DEFAULT_CUSTOM_PICK)
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
