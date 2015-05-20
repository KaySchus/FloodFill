from grid import Cell
from abc import ABCMeta, abstractmethod

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