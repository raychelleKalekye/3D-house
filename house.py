import cairo
import math
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

def draw_window(ctx, x, y, w, h, angle):
    ctx.save()
    ctx.scale(1.02, 0.98)
    # Translate the context to the desired position
    ctx.translate(x, y)
    # Apply the shear transformation for tilting
    ctx.transform(cairo.Matrix(1, math.tan(math.radians(angle)), 0, 1, 0, 0))
    # Draw the window
    ctx.rectangle(0, 0, w, h)
    ctx.set_source_rgb(50/255,203/255, 230/255)  # Light blue for window
    ctx.fill_preserve()
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(1) 
    ctx.stroke()
    ctx.restore()

# Draw the walls with hand-drawn effect
def draw_door(ctx):
    #door
    door_x, door_y = (450, 400)
    door_width, door_height = 100, 287
    ctx.rectangle(door_x, door_y, door_width, door_height)
    ctx.set_source_rgb(0.29, 0.21, 0.13)
    ctx.fill()
   #knob
    ctx.set_line_width(5)
    ctx.set_source_rgb(0.15, 0.1, 0)
    ctx.arc(door_x + 20, door_y + 120, 8, 0, 2 * math.pi)
    ctx.stroke()
    ctx.set_source_rgb(0.2, 0.1, 0)
    ctx.fill()
    #scribble
    ctx.set_line_width(4)
    ctx.set_source_rgb(0.2, 0.1, 0)
    ctx.move_to(door_x + 25, door_y + 30)
    ctx.curve_to(door_x + 40, door_y + 50, door_x + 40, door_y + 60, door_x + 70, door_y + 70)
    ctx.line_to(door_x + 25, door_y + 90)
    ctx.move_to(door_x + 25, door_y + 90)
    ctx.curve_to(door_x + 40, door_y + 110, door_x + 40, door_y + 120, door_x + 70, door_y + 130)
    ctx.line_to(door_x + 25, door_y + 150)  
    ctx.move_to(door_x + 25, door_y + 150)
    ctx.curve_to(door_x + 40, door_y + 170, door_x + 40, door_y + 180, door_x + 70, door_y + 190)
    ctx.line_to(door_x + 25, door_y + 210) 
    ctx.move_to(door_x + 25, door_y + 210)
    ctx.curve_to(door_x + 40, door_y + 230, door_x + 40, door_y + 240, door_x + 70, door_y + 250)
    ctx.line_to(door_x + 25, door_y + 250)  
   
    ctx.stroke()

# Draw the walls with hand-drawn effect
draw_base1(ctx)
draw_base2(ctx)
draw_door(ctx)

draw_window(ctx, 180, 360, 75, 120, 18)  # Right window
draw_window(ctx, 290, 390, 75, 120, 18)    # Door window
draw_window(ctx, 600, 450, 220, 100, 0)  # Left window


surface.write_to_png("3D-house.png")
