def addList(l1, l2):
	return (l1[0] + l2[0], l1[1] + l2[1])

def inBounds(grid, coords):
	if (coords[0] < grid.width and coords[1] < grid.height and coords[0] >= 0 and coords[1] >= 0):
		return True

	return False
