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
			print "North"
			self.grid.grid[location[0] + 1][location[1]] = Cell.RED
			location = (location[0] + 1, location[1])

		elif (south == Cell.BLANK):
			self.grid.grid[location[0] - 1][location[1]] = Cell.RED
			location = (location[0] - 1, location[1])
		
		elif (east == Cell.BLANK):
			self.grid.grid[location[0]][location[1] + 1] = Cell.RED
			location = (location[0], location[1] + 1)

		elif (west == Cell.BLANK):
			self.grid.grid[location[0]][location[1] - 1] = Cell.RED
			location = (location[0], location[1] - 1)

		else:
			return -1

		return location
