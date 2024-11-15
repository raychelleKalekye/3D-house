import cairo
import math

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1000, 1000)
ctx = cairo.Context(surface)




surface.write_to_png("3D-house.png")