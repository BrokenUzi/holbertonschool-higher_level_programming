#!/usr/bin/python3
""" Appends a string to the end of the UTF-8 file and returns # of chars that were implemented """

def append_write(filename="", text=""):
	""" Appends a string to the end of the UTF-8 file and returns # of chars that were implemented """
	with open(filename, 'a', encoding="utf-8") as NotAFileWinkWink:
		chars_added = NotAFileWinkWink.write(text)
	return chars_added
