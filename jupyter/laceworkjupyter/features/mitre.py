"""
File that provides access to Mitre ATT&CK data.
"""
import random
import string

import numpy as np
import pandas as pd

from taxii2client.v20 import Server
from stix2 import CompositeDataSource

from laceworkjupyter import manager
from laceworkjupyter import utils as main_utils
from laceworkjupyter.features import client
from laceworkjupyter.features import helper
from laceworkjupyter.features import utils


class MitreAttack:
    """
    Simple class that controls access to Mitre Att&ck datasets.
    """

    DEFAULT_SERVER = "https://cti-taxii.mitre.org/taxii/"

    def __init__(self):
        self._api_root = None
        self._server = None
        self._source = None
        self._frames = {}

    def _get_frame_from_collection(self, collection):
        """
        Returns a DataFrame with information from a Mitre Att&ck collection.
        """
        data = collection.get_objects()
        lines = []
        for item in data.get('objects', []):
            line = item
            external = item.get('external_references', [])
            for source in external:
                if not source.get("url", "").startswith("https://attack.mitre.org"):
                    continue
                line["mitre_source"] = source.get("source_name")
                line["mitre_id"] = source.get("external_id")
                url = source.get("url")
                url_items = url.split("/")
                line["mitre_collection"] = url_items[-2]
            lines.append(line)
        return pd.DataFrame(lines)

    @property
    def server(self):
        """
        Returns a copy of the Mitre server object.
        """
        if self._server:
            return self._server

        self._server = Server(self.DEFAULT_SERVER)
        self._api_root = self._server.api_roots[0]
        return self._server

    @property
    def collection_titles(self):
        """
        Returns a list of collection titles and ID that are available.
        """
        _ = self.server
        return [(c.title, c.id) for c in self._api_root.collections]

    @property
    def source(self):
        """
        Returns the data source object for Att&ck data.
        """
        if self._source:
            return self._source

        self._source = CompositeDataSource()
        self._source.add_data_sources(self._api_root.collections)

        return self._source

    def get_collection(self, collection_title):
        """
        Returns a DataFrame with the content of a particular collection.

        :param str collection_title: The tile or a substring of a collection
            entry in Mitre Att&ck framework. The first match of available
            collections will be used.
        :return: A pandas DataFrame with the content or an empty frame if the
            collection was not found.
        """
        _ = self.server
        for collection in self._api_root.collections:
            if collection_title.lower() not in collection.title.lower():
                continue

            title = collection.title
            if title not in self._frames:
                self._frames[title] = self._get_frame_from_collection(
                    collection)
            return self._frames[title]

        return pd.DataFrame()

    def get_technique(self, mitre_id, collection_title='Enterprise ATT&CK'):
        """
        Returns a pandas Series with the content of a single technique.

        :param str mitre_id: This is the corresponding Mitre Att&ck ID for the
            technique to look up.
        :param str collection_title: The title of the collection this
            particular technique exists in. By default uses the Enterprise
            collection.
        :return: A pandas Series with the information, or an empty series
            if not found.
        """
        titles = [x[0] for x in self.collection_titles]
        use_title = ""
        for title in titles:
            if collection_title.lower() in title.lower():
                use_title = title
                break
        if not use_title:
            raise ValueError("Collection Title %s not found", collection_title)

        if use_title not in self._frames:
            _ = self.get_collection(use_title)
        frame = self._frames.get(use_title)

        frame_slice = frame[frame.mitre_id == mitre_id.upper()]
        if not frame_slice.empty:
            return frame_slice.iloc[0].dropna()

        return pd.Series()


class FrameFilter:
    """
    Class for a frame filter.
    """

    def __init__(self, ctx, frame):
        self._ctx = ctx
        self._frame = frame
        self._temp_fields = []

    def _exact_filter(self, field_name, value):
        return self._frame[field_name] == value

    def _contains_filter(self, field_name, value):
        return self._frame[field_name].str.contains(value)

    def _re_filter(self, field_name, value):
        return self._frame[field_name].str.contains(value)

    def _get_random_string(self):
        return ''.join(
            random.choice(string.ascii_lowercase) for _ in range(6))

    def _get_field_name(self, field_dict):
        frame_field = field_dict.get('name', '')

        frame_column, _, json_fields = frame_field.partition('.')
        if not json_fields:
            return frame_column

        field_name = f'_temp_xtr_{self._get_random_string()}'
        self._frame[field_name] = self._frame[frame_column].apply(
            lambda x: helper.extract_json_field(x, json_fields))
        self._temp_fields.append(field_name)
        return field_name

    def get_filter(self, definition):
        filter_elements = []
        for field in definition.get('alert_fields', []):
            field_type = field.get('type', 'exact')
            field_name = self._get_field_name(field)
            value = field.get('value', '')

            if field_type == 'exact':
                filter_elements.append(self._exact_filter(field_name, value))
            elif field_type == 'contains':
                filter_elements.append(
                    self._contains_filter(field_name, value))
            elif field_type == 're':
                filter_elements.append(self._re_filter(field_name, value))

        condition = definition.get('condition', 'and')
        if len(filter_elements) == 1:
            return filter_elements[0]

        if condition == 'and':
            return np.logical_and.reduce(filter_elements)
        elif condition == 'or':
            return np.logical_or.reduce(filter_elements)

        return 'invalid'

    def cleanup(self):
        for field in self._temp_fields:
            del self._frame[field]

    def __enter__(self):
        """
        Support the with statement in python.
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Support the with statement in python.
        """
        self.cleanup()


@manager.register_feature
def get_mitre_client(ctx=None):
    """
    Returns a Mitre class object.
    """
    if ctx:
        mitre_client = ctx.get("mitre_client")
        if mitre_client:
            return mitre_client

        mitre_client = MitreAttack()
        ctx.add("mitre_client", mitre_client)
        return mitre_client

    return MitreAttack()


@manager.register_feature
def get_alerts_data_with_mitre(
        start_time="", end_time="", alert_frame=None, ctx=None):
    """
    Returns a DataFrame from the Alerts API call with Att&ck information.

    :param str start_time: The start time, in ISO format.
    :param str end_time: The end time, in ISO format.
    :param pandas.DataFrame alert_frame: An optional data frame with the
        results from the Alerts API call. If not provided the function
        will call the Alerts API to generate it.
    :return: A pandas DataFrame with the content of the Alerts API call
        merged with Att&CK information, if applicable.
    """
    if not ctx:
        raise ValueError("The context is required for this operation.")

    if alert_frame is None:
        lw_client = ctx.client
        if not lw_client:
            lw_client = client.get_client(ctx=ctx)

        default_start, default_end = main_utils.parse_date_offset(
            "LAST 2 DAYS")
        if not start_time:
            start_time = ctx.get("start_time", default_start)
        if not end_time:
            end_time = ctx.get("end_time", default_end)

        alert_df = lw_client.alerts.get(
            start_time=start_time, end_time=end_time)

    attack_mappings = utils.load_yaml_file("mitre.yaml")
    alert_df["mitre_id"] = np.nan
    with FrameFilter(ctx, alert_df) as frame_filter:
        for mapping in attack_mappings:
            my_filter = frame_filter.get_filter(mapping)
            alert_slice = alert_df[my_filter]
            if alert_slice.empty:
                continue
            alert_df.loc[my_filter, "mitre_id"] = mapping.get("id", np.nan)

    mitre_client = get_mitre_client(ctx=ctx)
    mitre_enterprise = mitre_client.get_collection("enterprise")
    mitre_preattack = mitre_client.get_collection("pre")

    first_merge = alert_df.merge(mitre_enterprise, on="mitre_id", how="left")
    return first_merge.merge(mitre_preattaack, on="mitre_id", how="left")
