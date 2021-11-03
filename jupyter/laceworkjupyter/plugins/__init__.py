"""A simple loading of plugins."""

from . import alert_rules
from . import datasources


PLUGINS = {
    'alert_rules.get': alert_rules.process_alert_rules,
    'datasources.list_data_sources': datasources.process_list_data_sources,
    'datasources.get_datasource_schema': datasources.process_datasource_schema,
}
