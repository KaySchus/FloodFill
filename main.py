#!/usr/bin/python

import sys
from State import Grid
from Generator import BoxGenerator, CaveGenerator
from Output import ImageWriter
from Simulation import FloodSimulator, RandomSimulator

image_title = sys.argv[1]

test = Grid(50, 50, ImageWriter("images/" + image_title))
test.setGenerator(BoxGenerator(test))
test.generate()

simulator = RandomSimulator(test)
simulator.simulate()

test.output()
