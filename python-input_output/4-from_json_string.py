#!/usr/bin/python3
""" Returns a py obj as a json str """

import json

def from_json_string(my_str):
	""" Returns a py obj as a json str """
	return json.loads(my_str)
