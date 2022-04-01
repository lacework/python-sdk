"""A simple loading of plugins."""

from . import alerts
from . import events
from . import evidence
from . import alert_rules
from . import datasources


PLUGINS = {
    'alerts.get': alerts.process_alerts,
    'alert_rules.get': alert_rules.process_alert_rules,
    'datasources.list_data_sources': datasources.process_list_data_sources,
    'datasources.get_datasource': datasources.process_datasource_schema,
    'events.get_details': events.process_event_details,
    'evidence.search': evidence.process_evidence_search,
}
