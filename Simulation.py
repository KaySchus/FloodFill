from PIL import Image, ImageDraw
from random import randint
from State import Grid, Cell
from MathUtils import addList, inBounds

class Location:
	def __init__(self, location, grid):
		self.location = location
		self.grid = grid

		self.north = Direction(addList(location, (0, 1)), self.grid)
		self.south = Direction(addList(location, (0, -1)), self.grid)
		self.east = Direction(addList(location, (1, 0)), self.grid)
		self.west = Direction(addList(location, (-1, 0)), self.grid)

		self.directions = (self.north, self.south, self.east, self.west)

	def isDirectionFree(self, location_str):
		if (location_str == "north"):
			if self.north.cell == Cell.BLANK:
				return True
			else:
				return False

		if (location_str == "south"):
			if (self.south.cell == Cell.BLANK):
				return True
			else:
				return False

		if (location_str == "east"):
			if (self.east.cell == Cell.BLANK):
				return True
			else:
				return False

		if (location_str == "west"):
			if (self.west.cell == Cell.BLANK):
				return True
			else:
				return False

	def hasFreeSpace(self):
		north_inbound = inBounds(self.grid, self.north.coords)
		south_inbound = inBounds(self.grid, self.south.coords)
		east_inbound = inBounds(self.grid, self.east.coords)
		west_inbound = inBounds(self.grid, self.west.coords)

		if ((self.north.cell == Cell.BLANK and north_inbound) or (self.south.cell == Cell.BLANK and south_inbound) or (self.east.cell == Cell.BLANK and east_inbound) or (self.west.cell == Cell.BLANK and west_inbound)):
			return True

		return False

	def getRandomDirection(self):
		direction_blank = False
		
		if (self.hasFreeSpace()):
			while direction_blank == False:
				selection = randint(0, 3)
				if (self.directions[selection].cell == Cell.BLANK and inBounds(self.grid, self.directions[selection].coords)):
					direction_blank = True

			return self.directions[selection]

		else:
			return -1

class Direction:
	def __init__(self, coords, grid):
		self.coords = coords
		
		if (inBounds(grid, coords)):
			self.cell = grid.getCell(coords)
		else:
			self.cell = Cell.WALL

class FloodSimulator:
	def __init__(self, grid):
		self.grid = grid

	def simulate(self):
		red_coords = self.find_start(Cell.RED)
		blue_coords = self.find_start(Cell.BLUE)

		print red_coords
		print blue_coords

		done = False

		while (done == False):
			if (red_coords != -1):
				red_coords = self.take_turn(red_coords, Cell.RED)

			if (blue_coords != -1):
				blue_coords = self.take_turn(blue_coords, Cell.BLUE)

			if (blue_coords == -1 and red_coords == -1):
				done = True

			self.grid.writer.save_frame(self.grid)

	def find_start(self, color):
		for y in range(self.grid.height):
			for x in range(self.grid.width):
				if (self.grid.getCell(x, y) == color):
					return (x, y)

		return -1

	def take_turn(self, coords, color):
		location = Location(coords, self.grid)

		if (location.isDirectionFree("north") and inBounds(self.grid, location.north.coords)):
			self.grid.setCell(location.north.coords, color)
			return location.north.coords

		elif (location.isDirectionFree("south") and inBounds(self.grid, location.south.coords)):
			self.grid.setCell(location.south.coords, color)
			return location.south.coords
		
		elif (location.isDirectionFree("east") and inBounds(self.grid, location.east.coords)):
			self.grid.setCell(location.east.coords, color)
			return location.east.coords

		elif (location.isDirectionFree("west") and inBounds(self.grid, location.east.coords)):
			self.grid.setCell(location.west.coords, color)
			return location.west.coords

		else:
			return -1

class RandomSimulator:
	def __init__(self, grid):
		self.grid = grid
		self.red_conv_coords = []
		self.blue_conv_coords = []

	def simulate(self):
		red_coords = self.find_start(Cell.RED)
		blue_coords = self.find_start(Cell.BLUE)

		self.red_conv_coords.append(red_coords)
		self.blue_conv_coords.append(blue_coords)

		done = False

		while (done == False):
			if (red_coords != -1):
				red_coords = self.take_turn(red_coords, Cell.RED)

				if (red_coords != -1):
					self.red_conv_coords.append(red_coords)
				else:
					location_found = False
					target = len(self.red_conv_coords) - 2

					while (location_found == False and target > 0):
						location = Location(self.red_conv_coords[target], self.grid)
						if (location.hasFreeSpace()):
							red_coords = location.location
							location_found = True
							print "Found free space back some squares (RED)"
						else:
							red_coords = -1
							print "No space found (RED)"

						target = target - 1

			if (blue_coords != -1):
				blue_coords = self.take_turn(blue_coords, Cell.BLUE)

				if (blue_coords != -1):
					self.blue_conv_coords.append(blue_coords)
				else:
					location_found = False
					target = len(self.blue_conv_coords) - 2

					while (location_found == False and target > 0):
						location = Location(self.blue_conv_coords[target], self.grid)
						if (location.hasFreeSpace()):
							blue_coords = location.location
							location_found = True
							print "Found free space back some squares (BLUE)"
						else:
							blue_coords = -1
							print "No space found (BLUE)"

						target = target - 1

			if (red_coords == -1 and blue_coords == -1):
				done = True

			self.grid.writer.save_frame(self.grid)

	def find_start(self, color):
		for y in range(self.grid.height):
			for x in range(self.grid.width):
				if (self.grid.getCell(x, y) == color):
					return (x, y)

		return -1

	def take_turn(self, coords, color):	
		location = Location(coords, self.grid)
		
		random_direction = location.getRandomDirection()

		if (random_direction != -1):
			self.grid.setCell(random_direction.coords, color)
			return random_direction.coords
		else:
			return -1
