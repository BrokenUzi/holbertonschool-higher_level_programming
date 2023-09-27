#!/usr/bin/python3
""" Adds args as a list then saves to a file """

import sys
import json

def save_to_json_file(my_obj, filename):
	with open(filename, 'w', encoding="utf-8") as NotAFileWinkWink:
		json.dump(my_obj, NotAFileWinkWink, ensure_ascii=False)

def load_from_json_file(filename):
	with open(filename, 'r', encoding="utf-8") as NotAFileWinkWink:
		data = json.load(NotAFileWinkWink)
	return data

arguments = sys.argv[1:]

try:
	existing_list = load_from_json_file('add_item.json')
except FileNotFoundError:
	existing_list = []

save_to_json_file(existing_list, 'add_item.json')
