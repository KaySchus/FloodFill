from PIL import Image, ImageDraw
from State import Grid, Cell

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
		north = (location[0], location[1] + 1)
		south = (location[0], location[1] - 1)
		east = (location[0] + 1, location[1])
		west = (location[0] - 1, location[1])

		if (self.grid.getCell(north) == Cell.BLANK):
			self.grid.setCell(north, Cell.RED)
			location = north

		elif (self.grid.getCell(south) == Cell.BLANK):
			self.grid.setCell(south, Cell.RED)
			location = south
		
		elif (self.grid.getCell(east) == Cell.BLANK):
			self.grid.setCell(east, Cell.RED)
			location = east

		elif (self.grid.getCell(west) == Cell.BLANK):
			self.grid.setCell(west, Cell.RED)
			location = west

		else:
			return -1

		return location
