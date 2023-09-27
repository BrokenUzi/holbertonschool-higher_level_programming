#!/usr/bin/python3
""" Reads a file """

def read_file(filename=""):
	""" Rwads UTF8 txt file """
	with open(filename, 'r' encoding="utf8") as NotAFileWinkWink:
		for line in NotAFileWinkWink:
			print(linje, end="")
