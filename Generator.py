from abc import ABCMeta, abstractmethod
from random import randint
from State import Cell

class Generator:
	__metaclass__ = ABCMeta

	@abstractmethod
	def generate(self, grid): pass

class BoxGenerator(Generator):
	def generate(self, grid):
		for y in range(grid.height):
			for x in range(grid.width):
				if ((x == 0) or (y == 0) or (x == grid.width - 1) or (y == grid.height - 1)):
					grid.setCell(x, y, Cell.WALL)
				else:
					grid.setCell(x, y, Cell.BLANK)

		x = randint(1, grid.width - 1)
		y = randint(1, grid.height - 1)

		grid.setCell(x, y, Cell.RED)

