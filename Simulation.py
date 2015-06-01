from PIL import Image, ImageDraw
from State import Grid, Cell
from MathUtils import addList

class Direction:
	def __init__(self, location, grid):
		self.location = location
		self.cell = grid.getCell(location)

class FloodSimulator:
	def __init__(self, grid):
		self.grid = grid

	def simulate(self):
		location = self.find_start()

		print location

		while (location != -1):
			location = self.take_turn(location)
			print location
			self.grid.writer.save_frame(self.grid)

	def find_start(self):
		for y in range(self.grid.height):
			for x in range(self.grid.width):
				if (self.grid.getCell(x, y) == Cell.RED):
					return (x, y)

		return -1

	def take_turn(self, location):
		north = Direction(addList(location, (0, 1)), self.grid)
		south = Direction(addList(location, (0, -1)), self.grid)
		east = Direction(addList(location, (1, 0)), self.grid)
		west = Direction(addList(location, (-1, 0)), self.grid)

		if (north.cell == Cell.BLANK):
			self.grid.setCell(north.location, Cell.RED)
			location = north.location

		elif (south.cell == Cell.BLANK):
			self.grid.setCell(south.location, Cell.RED)
			location = south.location
		
		elif (east.cell == Cell.BLANK):
			self.grid.setCell(east.location, Cell.RED)
			location = east.location

		elif (west.cell == Cell.BLANK):
			self.grid.setCell(west.location, Cell.RED)
			location = west.location

		else:
			return -1

		return location

class RandomSimulator:
	def __init__(self, grid):
		self.grid = grid

	def simulate(self):
		location = self.find_start()

		print location

		while location != -1:
			location = self.take_turn(location)
			print location
			self.grid.writer.save_frame(self.grid)

	def find_start(self):
		for y in range(self.grid.height):
			for x in range(self.grid.width):
				if (self.grid.getCell(x, y) == Cell.RED):
					return (x, y)

		return -1

	def take_turn(self, location):
		return location
