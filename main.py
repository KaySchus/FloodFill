#!/usr/bin/python

import grid
import generator

test = grid.Grid(256, 256, grid.ImageWriter("bars.png"), generator.BoxGenerator())
test.generate()
test.output()

