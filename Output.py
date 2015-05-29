from abc import ABCMeta, abstractmethod
from State import Grid
from PIL import Image, ImageDraw
from images2swf import writeSwf

class Writer:
	__metaclass__ = ABCMeta

	@abstractmethod
	def output(self): pass

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
		self.files = []

	def save_frame(self, grid):
		image = Image.new('RGBA', (grid.width, grid.height), (255, 255, 255, 0))
		draw = ImageDraw.Draw(image)

		for y in range(grid.height):
			for x in range(grid.width):
				point = grid.getCell(x, y)
				color = (255, 255, 255, 255)

				if (point == 1):
					color = (255, 0, 0, 255)

				if (point == 2):
					color = (0, 0, 255, 255)
	
				if (point == 3):
					color = (0, 0, 0, 255)

				draw.point((x, y), color)

		del draw
		self.files.append(image.resize((grid.width * 10, grid.height * 10), resample = Image.NEAREST))
		
	def output(self):
		writeSwf(self.filename, self.files, fps = 5, delays = None) 			
