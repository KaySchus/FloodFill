from abc import ABCMeta, abstractmethod
from random import randint
from State import Cell

class Generator:
	__metaclass__ = ABCMeta

	@abstractmethod
	def generate(self): pass

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
			self.grid.writer.save_frame(self.grid)
		
		suitable_space = False
		while suitable_space == False:
			new_location = (randint(1, self.grid.width - 1), randint(1, self.grid.height - 1))
			if self.grid.getCell(new_location) == Cell.BLANK:
				suitable_space = True

		self.grid.setCell(new_location, Cell.RED)
