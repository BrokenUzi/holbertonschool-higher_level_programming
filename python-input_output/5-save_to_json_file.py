#!/usr/bin/python3
""" Writes an obj to a text file JSON style """

import json

def save_to_json_file(my_obj, filename):
	""" Writes an obj to a text file JSON style """
	with open(filename, 'w', encoding="utf-8") as NotAFileWinkWink:
		json.dump(my_obj, NotAFileWinkWink, ensure_ascii=False)
