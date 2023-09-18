#!/usr/bin/python3
"Define a Square"

class Square:
	def __init__(self, size=0):
		self.size = size

if size < 0:
	print("size must be an integer")

elif size > 0:
	print("size must be >= 0")
