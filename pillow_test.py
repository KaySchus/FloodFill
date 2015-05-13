import os, sys
from PIL import Image, ImageDraw

image = Image.new('RGBA', (256, 256), (255, 255, 255, 0))

draw = ImageDraw.Draw(image)

for i in range(image.size[0]):
	for j in range(image.size[1]):
		draw.point((i, j), (i, j, 100, 255))

del draw

image.save("test.png", "PNG")



