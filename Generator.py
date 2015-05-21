from abc import ABCMeta, abstractmethod
from random import randint
from State import Cell

class Generator:
	__metaclass__ = ABCMeta

	@abstractmethod
	def generate(self, grid): pass

class BoxGenerator(Generator):
	def generate(self, grid):
		for i in range(grid.height):
			for j in range(grid.width):
				if ((j == 0) or (i == 0) or (j == grid.width - 1) or (i == grid.height - 1)):
					grid.grid[i][j] = Cell.WALL
				else:
					grid.grid[i][j] = Cell.BLANK

		x = randint(1, grid.width - 1)
		y = randint(1, grid.height - 1)

		grid.grid[y][x] = Cell.RED

