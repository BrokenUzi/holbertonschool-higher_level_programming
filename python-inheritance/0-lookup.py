#!/usr/bin/python3
def lookup(obj):
	""" Returns a list of available attributes """
	return [item for item in dir(obj) if not callable(getattr(obj, item))]
