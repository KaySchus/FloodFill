#!/usr/bin/python

from abc import ABCMeta, abstractmethod

class Cell:
	(BLANK, RED, BLUE, WALL) = (0, 1, 2, 3)

	def __init__(self):
		self.owner = Cell.BLANK

class Grid:
	def __init__(self, width, height, writer, generator):
		self.width = width
		self.height = height
		self.grid = [[Cell() for j in range(width)] for i in range(height)]
		self.writer = writer
		self.generator = generator

	def generate(self):
		self.generator.generate(self)

	def output(self):
		self.writer.output()

