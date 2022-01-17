"""Provides cloud hunting UI to construct LQL queries."""

import ipywidgets

from laceworkjupyter import manager
from laceworkjupyter.features import query_builder
from laceworkjupyter.features import utils


# The text displayed as the default table pick.
DEFAULT_TABLE_PICK = "Pick a table"
DEFAULT_CUSTOM_PICK = "Build A Custom Query"
DEFAULT_FILTER_PICK = "Pick what filters to include:"

# Since observation functions cannot pass arbitrary values
# we will need to make the LW context object global here.
lw_ctx = None


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
        state="query_builder", key="query_filters")
    for table_filter in table_filters:
        if table_filter.get("parameter", "N/A") == filter_name:
            filter_dict = table_filter
            break

    if not filter_dict:
        return

    box = lw_ctx.get_state(state="query_builder", key="query_filter_box")
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

    box = lw_ctx.get_state(state="query_builder", key="query_filter_box")

    if table_index == -1:
        # Default option, not a real table.
        box.children = []
        return

    tables = lw_ctx.get_state(
        state="query_builder", key="query_tables", default_value=[])

    if table_index == len(tables):
        query_builder.generate_table(lw_ctx)
        return

    # We now know we are not doing a custom table.
    lw_ctx.add_state("query_builder", "query_custom", False)

    try:
        table_name = tables[table_index].get("name")
    except IndexError:
        raise ValueError(
            "Table with index {0:d} is not defined.".format(table_index))

    if not table_name:
        raise ValueError("Invalid table")

    checkboxes = []
    table_filters = lw_ctx.get_state(
        state="query_builder", key="query_filters", default_value=[])
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


def _build_query(ctx):
    """
    Builds a LQL query from the query builder parameters.

    :param obj ctx: The Context object.
    """
    table_box = ctx.get_state(state="query_builder", key="query_table_box")
    table_widget = table_box.children[-1]
    value_widget = ctx.get_state(state="query_builder", key="query_filter_box")

    params = {}
    for child in value_widget.children:
        if not isinstance(child, ipywidgets.Text):
            continue
        params[child.description] = child.value

    query_dict = utils.get_query_definition(
        table_widget.value, params)
    query_name = query_dict.get("table_name", "No Table").replace(" ", "_")

    evaluator_id = query_dict.get("evaluator_id")
    lql_query = utils.build_lql_query(
        query_name, query_dict, join_support=False)
    ctx.add("lql_query", lql_query)
    ctx.add("lql_evaluator", evaluator_id)


def _verify_button(unused_button):
    """
    Handler for the verify button clicks.
    """
    global lw_ctx
    custom_query = lw_ctx.get_state("query_builder", key="query_custom")
    if custom_query:
        query_builder.build_query(lw_ctx)
    else:
        _build_query(lw_ctx)

    return query_builder.verify_query(lw_ctx)


def _execute_button(unused_button):
    """
    Handler for the execute button clicks.
    """
    global lw_ctx
    custom_query = lw_ctx.get_state("query_builder", key="query_custom")
    if custom_query:
        query_builder.build_query(lw_ctx)
    else:
        _build_query(lw_ctx)

    return query_builder.execute_query(lw_ctx)


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
        display="flex",
        flex_flow="column",
        align_items="stretch",
        width="1000px")

    title = ipywidgets.HTML(
        value=(
            "<div align=\"center\"><h1>Cloud Hunting</h1><i>Assistant to "
            "build LQL queries to perform threat hunting within your "
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

    ctx.add_state("query_builder", "query_table_box", table_box)
    ctx.add_state("query_builder", "query_start_widget", start_widget)
    ctx.add_state("query_builder", "query_end_widget", end_widget)
    ctx.add_state("query_builder", "query_filter_box", filter_box)
    ctx.add_state("query_builder", "query_label", result_label)

    ctx.add_state("query_builder", "query_tables", tables)
    ctx.add_state("query_builder", "query_filters", table_filters)
    lw_ctx = ctx
    query_builder.lw_ctx = ctx

    display(grid)  # noqa: F821
