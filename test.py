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
from auth import BoxAuthentication
'''
To start a test please create a Box account.
Create a Custom Application
get your client_id and access_token from the box admin console, and define client_secret and update config.py
If you want to use Summeyye's Custom Application credentials please ask to her.
'''
def main():
    # boxAuth = BoxAuthentication(client_id, client_secret, access_token)
    boxAuth = BoxAuthentication()
    print('Connect to Box')
    client = boxAuth.connect()
    user = client.user().get()
    print(user)
    print('The current user ID is {0}'.format(user.id))
    fm = FileManager(client)
    uploaded_file=fm.upload_file('test.png')
    print(uploaded_file)
    print('--')
    print(uploaded_file.id)
    
    ''' change download file path'''
    fm.download_file(uploaded_file.id,'/Users/your/Downloads/test_2020.png')


if __name__ == '__main__':
    main()