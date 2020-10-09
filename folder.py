from __future__ import print_function, unicode_literals
import os
from boxsdk import OAuth2, Client
from boxsdk.network.default_network import DefaultNetwork
from pprint import pformat
from boxsdk.exception import BoxAPIException
from boxsdk.object.collaboration import CollaborationRole
#from boxsdk.object.file as File

def get_folder_byname(client, folder_name):

	root_folder = client.folder('0')
	root_folder_with_info = root_folder.get()
	items = root_folder.get_items(limit=100, offset=0)
	for item in items:
		if item.name == folder_name:
			return item

	return create_folder(client,folder_name)

def create_folder(client,folderName):
	'''
	Create a subfolder with the given name in the folder.

	:param client:
		Client: authentication object
	:type client:
		:class: 'Client'
	:param folderName:
		The name of the new folder
	:return:
		A :class:'Folder' object with the given folder id.
    :rtype:
        :class:'Folder'
	'''

	subfolder = client.folder('0').create_subfolder(folderName)
	return subfolder

def list_folders(client, limit=None):
	'''
		Fetch all of the folders

		:param client:
			Client: authentication object
		:type client:
			:class: 'Client'
	    :returns:
            The collection of items in the folder.
        :rtype:
            `Iterable` of :class:`Item`
		'''
	max_num_of_folders=100
	if limit:
		max_num_of_folders = limit

	root_folder = client.folder('0')
	root_folder_with_info = root_folder.get()
	print(root_folder)
	print(root_folder_with_info)
	items = root_folder.get_items(limit=max_num_of_folders, offset=0)
	return items

def print_folders(client):
	'''
		Print all of the folders

		:param client:
			Client: authentication object
		:type client:
			:class: 'Client'
		'''
	root_folder = client.folder('0')
	root_folder_with_info = root_folder.get()
	print(root_folder)
	print(root_folder_with_info)
	items = root_folder.get_items(limit=100, offset=0)
	print('This is the first 100 items in the root folder:')
	for item in items:
		print(item)
