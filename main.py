#!/usr/bin/python

import sys
import grid
import generator

image_title = sys.argv[1]

test = grid.Grid(256, 256, grid.ImageWriter("images/" + image_title), generator.BoxGenerator())
test.generate()
test.output()

