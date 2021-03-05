# -*- coding: utf-8 -*-
import json
import logging
import os
import re
import requests

from collections import namedtuple
from github import Github

from laceworksdk.config import parse_conf_file

logger = logging.getLogger(__name__)


class ContentRepository():
    REPO_STANZA_RE = re.compile('^(?:(?:content_repository)|content_repository:(.+))$')
    DEFAULT_REPO_ID = '_default'
    DEFAULT_REPO_TYPE = 'github'
    DEFAULT_REPO_REF = 'main'

    POLICY = namedtuple('Policy', ['id', 'url', 'json', 'raw'])
    QUERY = namedtuple('Query', ['id', 'url', 'json', 'raw'])

    def __init__(
            self,
            session,
            config_file_path=None,
            typ=None,
            uri=None,
            ref=None,
            token=None):
        # {
        #     '<repo_id>': {
        #         'type': 'local|github',
        #         'uri': '<uri>',
        #         'token': '<token>',
        #         'ref': '<ref>'
        #     }
        # }
        self._session = session
        self.config_file_path = None
        self.repos = {}
        self.active_repo_id = None

        # 1. If configuration file exists, load it
        if isinstance(config_file_path, str) and os.path.isfile(config_file_path):
            self.config_file_path = os.path.realpath(config_file_path)
            config_items = parse_conf_file(self.config_file_path)
            self.load_config(config_items)

        # 2. Single instance mode
        elif uri and isinstance(uri, str):
            self.repos[self.DEFAULT_REPO_ID] = {
                'type': typ or self.DEFAULT_REPO_TYPE,
                'uri': uri,
                'token': token,
                'ref': ref or self.DEFAULT_REPO_REF,
            }
            self.active_repo_id = self.DEFAULT_REPO_ID

        assert self.repos, 'No content repositories found!'

        self.load_index()

    def load_config(self, config_items):
        '''
        [content_repository]
        active_repository = hazedav-private

        [content_repository:hazedav-private]
        type = github
        uri = hazedav/lacework-dev
        ref = main
        token = ****************************************
        '''
        for stanza, settings in config_items.items():
            stanza_match = self.REPO_STANZA_RE.match(stanza)

            if not stanza_match:
                continue

            try:
                repo_id = stanza_match.group(1)
                if not repo_id:
                    raise IndexError

                self.repos[repo_id] = {
                    'type': settings.get('type') or self.DEFAULT_REPO_TYPE,
                    'uri': settings.get('uri'),
                    'ref': settings.get('ref') or self.DEFAULT_REPO_REF,
                    'token': settings.get('token')
                }
            except IndexError:
                self.active_repo_id = settings.get('active_repository')

            if (self.repos
                    and self.active_repo_id
                    and self.active_repo_id in self.repos):
                return
            elif self.repos:
                # activate the first repository
                self.active_repo_id = list(self.repos)[0]

    def load_index(self):
        content_repo = self.repos[self.active_repo_id]

        if content_repo['type'] == 'github':
            content_file = ContentRepository.get_index_from_github(content_repo)
            self.index = json.loads(content_file.decoded_content.decode('utf-8'))
        else:
            raise NotImplementedError

    @staticmethod
    def get_index_from_github(content_repo):
        github_repo = Github(content_repo['token']).get_repo(content_repo['uri'])
        return github_repo.get_contents('content.index', ref=content_repo['ref'])

    def get_query(self, query_id):
        if self.repos[self.active_repo_id]['type'] == 'github':
            index_item = self.index['queries'][query_id]
            url = index_item[0]['url']

            headers = {
                'Accept': 'application/vnd.github.v3.raw',
            }
            if 'token' in self.repos[self.active_repo_id]:
                headers['Authorization'] = f'token {self.repos[self.active_repo_id]["token"]}'

            r = requests.get(
                url,
                headers=headers
            )
            # raise for 400/500
            r.raise_for_status()

            # load github blob using json and lower case all keys
            query_data = {k.lower(): v for k, v in json.loads(r.text).items()}

            return self.QUERY(
                id=query_id,
                url=url,
                json=query_data,
                raw=query_data['query_text']
            )
        else:
            raise NotImplementedError

    def get_policy(self, policy_id):
        if self.repos[self.active_repo_id]['type'] == 'github':
            index_items = self.index['policies'][policy_id]

            for index_item in index_items:
                url = index_item['url']

                headers = {
                    'Accept': 'application/vnd.github.v3.raw',
                }
                if 'token' in self.repos[self.active_repo_id]:
                    headers['Authorization'] = f'token {self.repos[self.active_repo_id]["token"]}'

                r = requests.get(
                    url,
                    headers=headers
                )
                # raise for 400/500
                r.raise_for_status()

                # load github blob using json and lower case all keys
                r_data = {k.lower(): v for k, v in json.loads(r.text).items()}

                if index_item['content_type'] == 'query':
                    query = self.QUERY(
                        id=index_item['id'],
                        url=index_item['url'],
                        json=r_data,
                        raw=r_data['query_text']
                    )
                elif index_item['content_type'] == 'policy':
                    policy = self.POLICY(
                        id=index_item['id'],
                        url=index_item['url'],
                        json=r_data,
                        raw=r_data
                    )
            return policy, query
        else:
            raise NotImplementedError

    def get_report(self, report_id):
        raise NotImplementedError
