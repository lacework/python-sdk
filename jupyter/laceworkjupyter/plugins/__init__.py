"""A simple loading of plugins."""

from . import alert_rules
from . import datasource


PLUGINS = {
    'alert_rules.get': alert_rules.process_alert_rules,
    'datasource.list_data_sources': datasource.process_list_data_sources,
    'datasource.get_datasource_schema': datasource.process_datasource_schema,
}
