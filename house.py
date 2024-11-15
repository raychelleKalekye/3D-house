import cairo
#import math
import random

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1000, 1000)
ctx = cairo.Context(surface)

# Background color
ctx.set_source_rgb(1, 1, 1)  # White background
ctx.paint()

def draw_base1(ctx):
    ctx.save()
    ctx.scale(1.02, 0.98)
    ctx.move_to(400, 700)      
    ctx.line_to(850, 700)       
    ctx.line_to(850, 330)      
    ctx.line_to(600, 180)       
    ctx.line_to(400, 330)       
    ctx.close_path()

    # Restore context to remove scaling before stroke
    ctx.restore()

    # Set fill color for wall
    ctx.set_source_rgb(0.9, 0.9, 0.9)
    ctx.fill_preserve()

    # Set varying stroke width to make it look hand-drawn
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(random.uniform(2, 4))  # Random stroke width for cartoon effect
    ctx.stroke()

def draw_base2(ctx):
    # Save context to apply transformations for hand-drawn effect
    ctx.save()
    # Apply slight scaling to create irregular "hand-drawn" effect
    ctx.scale(1.02, 0.98)
    # Adjusted coordinates for a narrower and slightly lower slant
    ctx.move_to(400, 700)        # Moved up from 750
    ctx.line_to(150, 600)        # Reduced width slightly from 100
    ctx.line_to(150, 230)        # Adjusted height to match the new slant
    ctx.line_to(400, 330)        # Kept aligned with base1 wall
    ctx.close_path()
    ctx.restore()
    # Set fill color for wall
    ctx.set_source_rgb(0.9, 0.9, 0.9)
    ctx.fill_preserve()

    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(random.uniform(2, 4))  
    ctx.stroke()

# Draw the walls with hand-drawn effect
draw_base1(ctx)
draw_base2(ctx)

surface.write_to_png("3D-house.png")