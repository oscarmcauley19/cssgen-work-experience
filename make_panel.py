#!/usr/bin/env dls-python2.7

from pkg_resources import require #imports require function from pkg_resources library
require('cssgen==0.4dls1') #runs require function with argument

from opimodel import widgets, colors, fonts, dls_utils #imports functions from opimodel library
from renderers.css import render #imports render function from renderer.css library


FILENAME = 'test.opi' #sets the target file in folder

colors.parse_css_color_file(dls_utils.find_color_file())


display = widgets.Display(588, 180) #sets display size
rectangle = widgets.Rectangle(0, 0, 50, 50) #makes rectangle variable 50x50px
display.add_child(rectangle) #uses add_child method to add rectangle to canvas

# Write out the display
render.get_opi_renderer(display).write_to_file(FILENAME)
