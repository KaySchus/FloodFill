#!/usr/bin/python

class Cell:
	def __init__(self):
		self.owner = 0

class Grid:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.grid = [[Cell() for j in range(width)] for i in range(height)]

	def output(self):
		for i in range(self.height):
			stored_output = ""

			for j in range(self.width):
				stored_output += str(self.grid[i][j].owner)
				stored_output += " "

			print "%s" % stored_output

