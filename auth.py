from __future__ import print_function, unicode_literals
import os
from boxsdk import OAuth2, Client
from boxsdk.network.default_network import DefaultNetwork
from pprint import pformat
from boxsdk.exception import BoxAPIException
from boxsdk.object.collaboration import CollaborationRole

import config
import folder

from filemanager import FileManager


class BoxAuthentication():

    def __init__(self):
        self.auth = OAuth2(
            client_id=config.CLIENT_ID,
            client_secret=config.CLIENT_SECRET,
            access_token=config.ACCESS_TOKEN,
        )
        self._client = None

    def connect(self):
        if not self._client:
            self._client = Client(self.auth)
        return self._client
