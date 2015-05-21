from abc import ABCMeta, abstractmethod
from State import Grid
from PIL import Image, ImageDraw

class Writer:
	__metaclass__ = ABCMeta

	@abstractmethod
	def output(self, gid): pass

class PrintWriter(Writer):
	def output(self, grid):
		for i in range(grid.height):
			stored_output = ""

			for j in range(grid.width):
				stored_output += str(grid.grid[i][j])
				stored_output += " "

			print "%s" % stored_output

class ImageWriter(Writer):
	def __init__(self, filename):
		self.filename = filename

	def output(self, grid):
		image = Image.new('RGBA', (grid.width, grid.height), (255, 255, 255, 0))
		draw = ImageDraw.Draw(image)

		for i in range(grid.height):
			for j in range(grid.width):
				point = grid.grid[i][j]
				color = (255, 255, 255, 255)

				if (point == 1):
					color = (255, 0, 0, 255)

				if (point == 2):
					color = (0, 0, 255, 255)
	
				if (point == 3):
					color = (0, 0, 0, 255)

				draw.point((i, j), color)

		del draw
		image.save(self.filename, "PNG")
					
