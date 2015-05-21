#!/usr/bin/python

import sys
from State import Grid
from Generator import BoxGenerator
from Output import ImageWriter

image_title = sys.argv[1]

test = Grid(256, 256, ImageWriter("images/" + image_title), BoxGenerator())
test.generate()
test.output()

