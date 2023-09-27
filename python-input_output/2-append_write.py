#!/usr/bin/python3
""" Appends a string to the end of the UTF-8 file and returns # of chars that were implemented """

def append_write(filename="", text=""):
	""" Appends a string to the end of the UTF-8 file and returns # of chars that were implemented """
	with open(filename, 'a', encoding="utf-8") as file:
		chars_added = file.write(text)
	return chars_added
