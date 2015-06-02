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
		self.cell = grid.getCell(coords)

class FloodSimulator:
	def __init__(self, grid):
		self.grid = grid

	def simulate(self):
		coords = self.find_start()

		print coords

		while (coords != -1):
			coords = self.take_turn(coords)
			print coords
			self.grid.writer.save_frame(self.grid)

	def find_start(self):
		for y in range(self.grid.height):
			for x in range(self.grid.width):
				if (self.grid.getCell(x, y) == Cell.RED):
					return (x, y)

		return -1

	def take_turn(self, coords):
		location = Location(coords, self.grid)

		if (location.isDirectionFree("north") and inBounds(self.grid, location.north.coords)):
			self.grid.setCell(location.north.coords, Cell.RED)
			return location.north.coords

		elif (location.isDirectionFree("south") and inBounds(self.grid, location.south.coords)):
			self.grid.setCell(location.south.coords, Cell.RED)
			return location.south.coords
		
		elif (location.isDirectionFree("east") and inBounds(self.grid, location.east.coords)):
			self.grid.setCell(location.east.coords, Cell.RED)
			return location.east.coords

		elif (location.isDirectionFree("west") and inBounds(self.grid, location.east.coords)):
			self.grid.setCell(location.west.coords, Cell.RED)
			return location.west.coords

		else:
			return -1

class RandomSimulator:
	def __init__(self, grid):
		self.grid = grid
		self.converted_coords = []

	def simulate(self):
		coords = self.find_start()

		self.converted_coords.append(coords)

		while (coords != -1):
			coords = self.take_turn(coords)

			if (coords != -1):
				self.converted_coords.append(coords)
			else:
				count = -2
				no_place_found = True
				while (count > (len(self.converted_coords) * -1) and no_place_found == True):
					location = Location(self.converted_coords[count], self.grid)
					print count
					count -= 1
					if (location.hasFreeSpace()):
						coords = location.getRandomDirection().coords
						no_place_found = False

			self.grid.writer.save_frame(self.grid)

	def find_start(self):
		for y in range(self.grid.height):
			for x in range(self.grid.width):
				if (self.grid.getCell(x, y) == Cell.RED):
					return (x, y)

		return -1

	def take_turn(self, coords):	
		location = Location(coords, self.grid)
		
		random_direction = location.getRandomDirection()

		if (random_direction != -1):
			self.grid.setCell(random_direction.coords, Cell.RED)
			return random_direction.coords
		else:
			return -1
