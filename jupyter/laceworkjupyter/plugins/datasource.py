"""An output plugin for the Lacework DataSource API."""


import pandas as pd


def process_list_data_sources(data):
    """
    Returns a Pandas DataFrame from the API call.

    :return: A pandas DataFrame.
    """
    lines = [{'name': x, 'description': y} for x, y in data]
    return pd.DataFrame(lines)


def process_datasource_schema(data):
    """
    Returns a Pandas DataFrame from the output of the API call.
    """
    data_dict = data.get('data', {})
    schemas = data_dict.get('resultSchema', [])

    return pd.DataFrame(schemas)

    """
    get_datasource_schema
                     name              description                                       resultSchema
0  LW_HA_DNS_REQUESTS  DNS Request information  {'name': 'BATCH_START_TIME', 'dataType': 'Time...

{'data': {'name': 'LW_HA_DNS_REQUESTS',
  'description': 'DNS Request information',
  'resultSchema': [{'name': 'BATCH_START_TIME',
    'dataType': 'Timestamp',
    'description': 'Beginning of time interval'},
   {'name': 'BATCH_END_TIME',
    'dataType': 'Timestamp',
    'description': 'End of time interval'},
   {'name': 'RECORD_CREATED_TIME',
    'dataType': 'Timestamp',
    'description': 'Record creation time'},
   {'name': 'MID',
    'dataType': 'Number',
    'description': 'Machine ID reporting the activity'},
   {'name': 'SRV_IP_ADDR',
    'dataType': 'String',
    'description': 'IP address of DNS Server'},
   {'name': 'HOSTNAME',
    'dataType': 'String',
    'description': 'Hostname that is being looked up'},
   {'name': 'HOST_IP_ADDR',
    'dataType': 'String',
    'description': 'Resolved IP address of hostname'},
   {'name': 'TTL',
    'dataType': 'Number',
    'description': 'Time to live for name resolution'},
   {'name': 'PKTLEN',
    'dataType': 'Number',
    'description': 'Length of response packet'}]}}
    """
