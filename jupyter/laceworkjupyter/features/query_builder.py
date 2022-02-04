"""Provides UI to construct LQL queries."""

import ipywidgets

from laceworksdk import http_session
from laceworkjupyter import manager
from laceworkjupyter.features import utils


# The text displayed as the default table pick.
DEFAULT_TABLE_PICK = "Pick a table"
DEFAULT_FILTER_PICK = "Pick what filters to include:"

DEFAULT_FILTER_BEHAVIOR = {
    "String": {
        "Equals": "{attribute:s} = '{value:s}'",
        "Contains": "{attribute:s} LIKE '%{value:s}%'",
        "Not Contains": "{attribute:s} NOT LIKE '%{value:s}%'",
        "Exists": "{attribute:s} IS NOT NULL"},
    "JSON": {
        "Equals": "{attribute:s}:{key:s} = '{value:s}'",
        "Contains": "{attribute:s}:{key:s} LIKE '%{value:s}%'",
        "Not Contains": "{attribute:s}:{key:s} NOT LIKE '%{value:s}%'",
        "Exists": "{attribute:s}:{key:s} IS NOT NULL"},
    "Number": {
        "Equals": "{attribute:s} = {value:s}",
        "Less Than": "{attribute:s} <= {value:s}",
        "Greater Than": "{attribute:s} >= {value:s}"},
    "Defaults": {
        "String": "Contains",
        "JSON": "Contains",
        "Number": "Equals"}
}

# Since observation functions cannot pass arbitrary values
# we will need to make the LW context object global here.
lw_ctx = None


def add_filter_definition(change):
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

    box = lw_ctx.get_state(state="query_builder", key="query_filter_box")
    children = list(box.children)

    table_schema_dict = lw_ctx.get_state(
        state="query_builder", key="query_custom_table_schema")
    schema = table_schema_dict.get(parameter_name, {})
    schema_type = schema.get("data_type", "String")
    filter_behavior = DEFAULT_FILTER_BEHAVIOR.get(schema_type)
    dropdown_options = filter_behavior.keys()
    dropdown_default = DEFAULT_FILTER_BEHAVIOR["Defaults"].get(schema_type)

    # We give each character 12px in size, which should be an ample space
    # for it to be displayed.
    parameter_width = len(parameter_name) * 12
    dropdown_width = max([len(x) for x in dropdown_options]) * 12

    layout = ipywidgets.Layout(height="auto", width="100%")
    if filter_display:
        filter_children = [
            ipywidgets.Label(
                parameter_name,
                layout=ipywidgets.Layout(
                    width=f"{parameter_width}px")),
            ipywidgets.Dropdown(
                options=dropdown_options,
                value=dropdown_default,
                description="",
                layout=ipywidgets.Layout(
                    width=f"{dropdown_width}px"),
                disabled=False),
            ipywidgets.Text(
                value="",
                placeholder="Type A Filter Value",
                description="",
                disabled=False
            )]

        # Special handling for JSON.
        if schema_type == "JSON":
            filter_children.insert(1, ipywidgets.Text(
                value="", placeholder="Attribute Name",
                description="", disabled=False))

        new_box = ipywidgets.HBox(children=filter_children, layout=layout)
        children.append(new_box)
    else:
        new_children = []
        for child in children:
            if not isinstance(child, ipywidgets.HBox):
                new_children.append(child)
                continue

            box_children = child.children
            if len(box_children) not in (3, 4):
                new_children.append(child)
                continue

            label_widget = box_children[0]
            if label_widget.value != parameter_name:
                new_children.append(child)
        children = new_children

    box.children = children


def generate_table(ctx):
    """
    Adds a list of tables and associated filters.
    """
    box = ctx.get_state(state="query_builder", key="query_filter_box")
    datasources = ctx.client.datasources.get()
    ctx.add_state("query_builder", "query_datasources", datasources)
    ctx.add_state("query_builder", "query_custom", True)

    tables = {x["description"]: x["name"] for _, x in datasources.iterrows()}
    options = [DEFAULT_TABLE_PICK]
    options.extend(tables.keys())
    table_list = ipywidgets.Dropdown(
        options=options,
        description="Choose table",
        disabled=False
    )
    table_list.observe(generate_filters)

    children = [
        ipywidgets.Label("Available Tables to Query From:"),
        table_list
    ]
    box.children = children


def generate_filters(change):  # noqa: C901
    """
    Adds all filters that belong to a custom table.
    """
    global lw_ctx

    if change["type"] != "change":
        return
    if change["name"] != "index":
        return

    box = lw_ctx.get_state(state="query_builder", key="query_filter_box")
    datasources = lw_ctx.get_state("query_builder", key="query_datasources")
    table_index = change.get("new", 0)

    # We added a default text as the first option.
    table_index -= 1

    try:
        datasource = datasources.iloc[table_index]
    except IndexError:
        raise ValueError(
            "Table with index {0:d} is not defined.".format(table_index))

    table_name = datasource['name']
    lw_ctx.add_state("query_builder", "query_custom_table_name", table_name)

    table_schema = lw_ctx.client.datasources.get_datasource(table_name)

    checkboxes = []
    return_fields = []

    layout = ipywidgets.Layout(height="auto", width="90%")
    table_schema_dict = {}
    for _, row in table_schema.iterrows():
        name = row["name"]
        return_fields.append(name)
        data_type = row["dataType"]
        description = row["description"]
        table_schema_dict[name] = {
            "data_type": data_type,
            "description": description
        }

        # We don't support Timestamp filters.
        if data_type == "Timestamp":
            continue

        checkboxes.append(
            ipywidgets.Checkbox(
                value=False,
                layout=layout,
                description=f"{name} [{data_type}] - {description}"))

    lw_ctx.add_state(
        "query_builder", "query_custom_return_fields", return_fields)
    lw_ctx.add_state(
        "query_builder", "query_custom_table_schema", table_schema_dict)

    for checkbox in checkboxes:
        checkbox.observe(add_filter_definition)

    children = list(box.children)
    for index, child in enumerate(children):
        if isinstance(child, ipywidgets.Label):
            if child.value == DEFAULT_FILTER_PICK:
                children = children[:index]
                break

    children.append(ipywidgets.Label(DEFAULT_FILTER_PICK))
    children.extend(checkboxes)
    children.append(ipywidgets.Label(
        "Add the values for each selected filter (all filters "
        "have AND conditions between them):"))
    box.children = children


def build_query(ctx):
    """
    Builds a LQL query from the query builder parameters.

    :param obj ctx: The Context object.
    """
    value_widget = ctx.get_state(
        state="query_builder", key="query_filter_box")
    table_schema_dict = ctx.get_state(
        state="query_builder", key="query_custom_table_schema")

    filters = []
    for child in value_widget.children:
        if not isinstance(child, ipywidgets.HBox):
            continue
        label_widget = child.children[0]
        attribute = label_widget.value
        attribute_schema = table_schema_dict.get(attribute, "")

        if not attribute_schema:
            raise ValueError("Unable to handle data of type for {0:s}".format(
                attribute))

        attribute_type = attribute_schema.get("data_type", "String")

        if attribute_type == "JSON":
            key_widget = child.children[1]
            key = key_widget.value
            dropdown_widget = child.children[2]
            text_widget = child.children[3]
        else:
            dropdown_widget = child.children[1]
            text_widget = child.children[2]
            key = ""

        filter_behavior = DEFAULT_FILTER_BEHAVIOR.get(
            attribute_type, {})
        filter_format_string = filter_behavior.get(
            dropdown_widget.value, "{attribute} = {value:s}")

        filter_string = filter_format_string.format(
            attribute=attribute, value=text_widget.value, key=key)
        filters.append(filter_string)

    query_dict = {
        "table_name": ctx.get_state(
            state="query_builder", key="query_custom_table_name"),
        "filters": filters,
        "return_fields": ctx.get_state(
            state="query_builder", key="query_custom_return_fields"),
    }

    if query_dict.get("table_name", "") == "CloudTrailRawEvents":
        evaluator_id = "Cloudtrail"
    else:
        evaluator_id = None

    lql_query = utils.build_lql_query("CustomQueryBuild", query_dict)
    ctx.add("lql_query", lql_query)
    ctx.add("lql_evaluator", evaluator_id)


def verify_query(ctx):
    """
    Verify a LQL query.
    """
    label_widget = ctx.get_state(state="query_builder", key="query_label")
    lql_query = ctx.get("lql_query")
    evaluator_id = ctx.get("lql_evaluator")

    try:
        _ = ctx.client.queries.validate(
            lql_query, evaluator_id=evaluator_id)
    except http_session.ApiError as err:
        label_widget.value = "Failure to verify: {0}".format(err)
        return False

    label_widget.value = "LQL Verified."
    return True


def execute_query(ctx):
    """
    Verify and execute a LQL query.
    """
    if not verify_query(ctx):
        return

    lql_query = ctx.get("lql_query")
    lql_evaluator = ctx.get("lql_evaluator")

    label_widget = ctx.get_state(state="query_builder", key="query_label")
    label_widget.value = (
        f"{label_widget.value}.<br/><br/><b>Executing query...</b>")

    start_time, end_time = utils.get_times_from_widgets(ctx)
    arguments = {
        "StartTimeRange": start_time,
        "EndTimeRange": end_time
    }

    df = ctx.client.queries.execute(
        evaluator_id=lql_evaluator, query_text=lql_query, arguments=arguments)

    ctx.add("lql_results", df)
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


def _verify_button(unused_button):
    """
    Handler for the verify button clicks.
    """
    global lw_ctx
    build_query(lw_ctx)
    return verify_query(lw_ctx)


def _execute_button(unused_button):
    """
    Handler for the execute button clicks.
    """
    global lw_ctx
    build_query(lw_ctx)
    return execute_query(lw_ctx)


@manager.register_feature
def query_builder(ctx=None):
    """
    Displays a UI to build LQL queries.
    """
    global lw_ctx  # To be able to pass the grid to widget functions.

    verify_button = ipywidgets.Button(
        value=False,
        description="Verify Query",
        disabled=False,
        tooltip="Build the LQL query and verify it",
        icon="check"
    )
    verify_button.on_click(_verify_button)

    execute_button = ipywidgets.Button(
        value=False,
        description="Execute Query",
        button_style="success",
        disabled=False,
        tooltip="Build the LQL query and execute it"
    )
    execute_button.on_click(_execute_button)

    box_layout = ipywidgets.Layout(
        display='flex',
        flex_flow='column',
        align_items='stretch',
        width='1000px')

    title = ipywidgets.HTML(
        value=(
            "<div align=\"center\"><h1>Query Builder</h1><i>Assistant to "
            "build LQL queries to query data within your "
            "environment.</i><br/><br/></div>"))

    start_time, end_time = utils.get_start_and_end_time(ctx)
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

    ctx.add_state("query_builder", "query_start_widget", start_widget)
    ctx.add_state("query_builder", "query_end_widget", end_widget)
    ctx.add_state("query_builder", "query_filter_box", filter_box)
    ctx.add_state("query_builder", "query_label", result_label)
    lw_ctx = ctx

    generate_table(ctx)
    display(grid)  # noqa: F821
