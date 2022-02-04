"""
File that provides access to Mitre ATT&CK data.
"""

import pandas as pd

from taxii2client.v20 import Server
from stix2 import CompositeDataSource

from laceworkjupyter import manager
from laceworkjupyter import utils as main_utils
from laceworkjupyter.features import client
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
def get_alerts_data_with_mitre(start_time="", end_time="", ctx=None):
    """
    Returns a DataFrame from the Alerts API call with Att&ck information.

    :param str start_time: The start time, in ISO format.
    :param str end_time: The end time, in ISO format.
    :return: A pandas DataFrame with the content of the Alerts API call
        merged with Att&CK information, if applicable.
    """
    if not ctx:
        raise ValueError("The context is required for this operation.")

    attack_mappings = pd.DataFrame(utils.load_yaml_file("mitre.yaml"))
    mitre_client = get_mitre_client(ctx=ctx)
    mitre_enterprise = mitre_client.get_collection("enterprise")
    mitre_joined_df = attack_mappings.merge(mitre_enterprise, how="left")

    lw_client = ctx.client
    if not lw_client:
        lw_client = client.get_client()

    default_start, default_end = main_utils.parse_date_offset("LAST 2 DAYS")
    if not start_time:
        start_time = ctx.get("start_time", default_start)
    if not end_time:
        end_time = ctx.get("end_time", default_end)

    alert_df = lw_client.alerts.get(start_time=start_time, end_time=end_time)
    return alert_df.merge(mitre_joined_df, how="left")
