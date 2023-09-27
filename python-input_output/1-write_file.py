#!/usr/bin/python3
""" Write File writes a string inside a textfile in UTF-8 """

def write_file(filename="", text=""):
	"""  Write File writes a string inside a textfile in UTF-8 """
	with open(filename, 'w', encoding="utf-8") as NotAFileWinkWink:
		chars_written = NotAFileWinkWink.write(text)
	return chars_written
