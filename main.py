#!/usr/bin/python

import sys
from State import Grid
from Generator import BoxGenerator
from Output import ImageWriter
from Simulation import FloodSimulator

image_title = sys.argv[1]

test = Grid(20, 20, ImageWriter("images/" + image_title), BoxGenerator())
test.generate()

simulator = FloodSimulator(test)
simulator.simulate()

test.output()
