#!/usr/bin/python

import os, sys
from abc import ABCMeta, abstractmethod
from PIL import Image, ImageDraw

class Cell:
	def __init__(self):
		self.owner = 0

class Grid:
	def __init__(self, width, height, writer):
		self.width = width
		self.height = height
		self.grid = [[Cell() for j in range(width)] for i in range(height)]
		self.writer = writer

	def output(self):
		self.writer.output(self)

class Writer:
	__metaclass__ = ABCMeta

	@abstractmethod
	def output(self, grid): pass

class PrintWriter(Writer):
	def output(self, grid):
		for i in range(grid.height):
			stored_output = ""

			for j in range(grid.width):
				stored_output += str(grid.grid[i][j].owner)
				stored_output += " "

			print "%s" % stored_output

class ImageWriter(Writer):
	def __init__(self, filename):
		self.filename = filename

	def output(self, grid):
		image = Image.new('RGBA', (grid.width, grid.height), (255, 255, 255, 0))
		draw = ImageDraw.Draw(image)

		for i in range(grid.width):
			for j in range(grid.height):
				if (grid.grid[i][j] == 0):
					draw.point((i, j), (255, 255, 255, 0))

				if (grid.grid[i][j] == 1):
					draw.point((i, j), (255, 0, 0, 0))

				if (grid.grid[i][j] == 2):
					draw.point((i, j), (0, 0, 255, 0))

				if (grid.grid[i][j] >= 3):
					draw.point((i, j), (0, 0, 0, 0))

		del draw

		image.save(self.filename, "PNG")
