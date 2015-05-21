from PIL import Image, ImageDraw
from State import Grid, Cell

class FloodSimulator:
	def __init__(self, grid):
		self.grid = grid

	def simulate(self):
		location = self.find_start()

		print location

	def find_start(self):
		for i in range(self.grid.height):
			for j in range(self.grid.width):
				if (self.grid.grid[i][j] == Cell.RED):
					return (i, j)

		return (-1, -1)
