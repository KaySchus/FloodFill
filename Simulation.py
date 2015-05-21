from PIL import Image, ImageDraw
from State import Grid, Cell

class FloodSimulator:
	def __init__(self, grid):
		self.grid = grid

	def simulate(self):
		location = self.find_start()

		print location

		loop_count = 0
		filename = self.grid.writer.filename
		filename_parts = filename.split('.')

		while (location != -1):
			location = self.take_turn(location)
			self.grid.writer.filename = filename_parts[0] + "_" + str(loop_count) + "." + filename_parts[1]
			self.grid.output()
			loop_count += 1

	def find_start(self):
		for i in range(self.grid.height):
			for j in range(self.grid.width):
				if (self.grid.grid[i][j] == Cell.RED):
					return (i, j)

		return (-1, -1)

	def take_turn(self, location):
		north = self.grid.grid[location[0] + 1][location[1]]
		south = self.grid.grid[location[0] - 1][location[1]]
		east = self.grid.grid[location[0]][location[1] + 1]
		west = self.grid.grid[location[0]][location[1] - 1]

		if (north == Cell.BLANK):
			north = Cell.RED
			location += (1, 0)

		elif (east == Cell.BLANK):
			east = Cell.RED
			location += (0, 1)
		
		elif (south == Cell.BLANK):
			south = Cell.RED
			location += (-1, 0)

		elif (west == Cell.BLANK):
			west = Cell.RED
			location += (0, -1)

		else:
			return -1

		return location
