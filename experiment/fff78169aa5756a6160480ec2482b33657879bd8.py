# Trying to implement a colour wheel
# Jim Grange (www.jimgrange.wordpress.com)
# December 2016

#==================================================
# import required libraries
#==================================================
import random
import os
import numpy as np 
from numpy import sin, cos, radians, deg2rad
from psychopy import visual, data, event, gui, core

#==================================================
# experiment parameters & create stimuli
#==================================================

# size of stimulus
stim_size = 200

# radius of colour wheel
colour_radius = stim_size / 2

# number of colours
n_colours = 360

#==================================================
# create window & generate stim containers
#==================================================
scrsize = (600, 400)
win = visual.Window(size = scrsize, color = (0.6, 0.6, 0.6), units = 'pix', fullscr = False)


# decalre one line which will represent each colour component of the wheel.
stim = visual.Line(win, units = 'pix', start = (0, 0))



#==================================================
# run experiment
#==================================================

# draw the welcome screen
win.mouseVisible = False

# draw the colour wheel
for curr_colour in range(n_colours):
    
    # get the current degrees in radians
    colour_radians = deg2rad(curr_colour)
    
    # calculate the x and y end points of the line for the circle
    x_pos = colour_radius * cos(colour_radians)
    y_pos = colour_radius * sin(colour_radians)
    
    # set the characteristics of the line and draw it
    stim.setLineColor([curr_colour, 1, 1], colorSpace = 'hsv')
    stim.setEnd([y_pos, x_pos])
    stim.draw()

win.flip()
keys = event.waitKeys(keyList = ['space', 'escape'])