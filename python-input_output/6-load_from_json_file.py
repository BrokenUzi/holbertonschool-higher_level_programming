#!/usr/bin/python3
""" Creates an obj from JSON file """

import json

def load_from_json_file(filename):
	""" Creates an obj from JSON file """
	with open(filename, 'r', encoding="utf-8") as NotAFileWinkWink:
		data = json.load(NotAFileWinkWink)
	return data
