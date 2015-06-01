#!/usr/bin/python

import sys
from State import Grid
from Generator import CaveGenerator
from Output import ImageWriter
from Simulation import FloodSimulator

image_title = sys.argv[1]

test = Grid(100, 100, ImageWriter("images/" + image_title))
test.setGenerator(CaveGenerator(test, 20))
test.generate()

simulator = FloodSimulator(test)
simulator.simulate()

test.output()
