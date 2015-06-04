from abc import ABCMeta, abstractmethod
from random import randint
from State import Cell

def set_free_space(grid, color):	
	suitable_space = False
	while suitable_space == False:
		new_location = (randint(1, grid.width - 1), randint(1, grid.height - 1))
		if grid.getCell(new_location) == Cell.BLANK:
			suitable_space = True

	grid.setCell(new_location, color)

class Generator:
	__metaclass__ = ABCMeta

	@abstractmethod
	def generate(self): pass

class BoxGenerator(Generator):
	def __init__(self, grid):
		self.grid = grid

	def generate(self):
		for y in range(self.grid.height):
			for x in range(self.grid.width):
				if ((x == 0) or (y == 0) or (x == self.grid.width - 1) or (y == self.grid.height - 1)):
					self.grid.setCell(x, y, Cell.WALL)
				else:
					self.grid.setCell(x, y, Cell.BLANK)

		set_free_space(self.grid, Cell.RED)
		set_free_space(self.grid, Cell.BLUE)

class CaveGenerator(Generator):
	def __init__(self, grid, numpasses):
		self.grid = grid
		self.max_pass = numpasses

	def seed(self):
		for y in range(self.grid.height):
			for x in range(self.grid.width):
				if randint(0, 1) == 1:
					self.grid.setCell(x, y, Cell.WALL)

	def smooth(self):
		new_cells = [[Cell() for x in range(self.grid.width)] for y in range(self.grid.height)]		

		for y in range(self.grid.height):
			for x in range(self.grid.width):
				value = 0

				if (self.grid.getCell(x, y) == Cell.WALL):
					value += 1
				else:
					value -= 1

				if (x != 0):
					if (self.grid.getCell(x - 1, y) == Cell.WALL):
						value += 1
					else:
						value -= 1

				if (y != 0):
					if (self.grid.getCell(x, y - 1) == Cell.WALL):
						value += 1
					else:
						value -= 1

				if (x != 0 and y != 0):
					if (self.grid.getCell(x - 1, y - 1) == Cell.WALL):
						value += 1
					else:
						value -= 1
							
				if (x != self.grid.width - 1):
					if (self.grid.getCell(x + 1, y) == Cell.WALL):
						value += 1
					else:
						value -= 1

				if (y != self.grid.height - 1):
					if (self.grid.getCell(x, y + 1) == Cell.WALL):
						value += 1
					else:
						value -= 1

				if (x != self.grid.width - 1 and y != 0):
					if (self.grid.getCell(x + 1, y - 1) == Cell.WALL):
						value += 1
					else:
						value -= 1

				if (x != 0 and y != self.grid.height - 1):
					if (self.grid.getCell(x - 1, y + 1) == Cell.WALL):
						value += 1
					else:
						value -= 1

				if (x != self.grid.width - 1 and y != self.grid.height - 1):
					if (self.grid.getCell(x + 1, y + 1) == Cell.WALL):
						value += 1
					else:
						value -= 1

				if (value > 0):
					new_cells[y][x] = Cell.WALL
				else:
					new_cells[y][x] = Cell.BLANK

		for y in range(self.grid.height):
			for x in range(self.grid.width):
				self.grid.setCell(x, y, new_cells[y][x])

	def generate(self):
		self.seed()
	
		self.grid.writer.save_frame(self.grid)	

		for i in range(self.max_pass):
			self.smooth()
		
		set_free_space(self.grid, Cell.RED)
		set_free_space(self.grid, Cell.BLUE)
