#!/usr/bin/python3
""" Reads a file """

def read_file(filename=""):
	""" Reads UTF-8 txt file """
	with open(filename, 'r', encoding="utf-8") as NotAFileWinkWink:
		for line in NotAFileWinkWink:
			print(line, end="")
