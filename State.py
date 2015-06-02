#!/usr/bin/python

from abc import ABCMeta, abstractmethod

class Cell:
	(BLANK, RED, BLUE, WALL) = (0, 1, 2, 3)

	def __init__(self):
		self.owner = Cell.BLANK

class Grid:
	def __init__(self, width, height, writer):
		self.width = width
		self.height = height
		self.cells = [[Cell() for j in range(width)] for i in range(height)]
		self.writer = writer

	def setGenerator(self, generator):
		self.generator = generator

	def generate(self):
		self.generator.generate()

	def output(self):
		self.writer.output()

	def getCell(self, *args):
		if len(args) == 1:
			return self.cells[args[0][1]][args[0][0]]
		elif len(args) == 2:
			return self.cells[args[1]][args[0]]
		else:
			print "Incorrect getCell(...) usage"
	
	def setCell(self, *args):
		if len(args) == 2:
			self.cells[args[0][1]][args[0][0]] = args[1]
		elif len(args) == 3:
			self.cells[args[1]][args[0]] = args[2]
		else:
			print "Incorrect setCell(...) usage"
