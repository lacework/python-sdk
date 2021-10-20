"""A simple loading of plugins."""

from . import datasource


PLUGINS = {
    'datasource.list_data_sources': datasource.process_list_data_sources,
    'datasource.get_datasource_schema': datasource.process_datasource_schema,
}
