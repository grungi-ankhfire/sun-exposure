#!BPY
"""Registration info for Blender menus:
Name: 'Exposure'
Blender: 249
Group: 'Wizards'
Tooltip: 'Calculate whether points in a scene are lit or in the shadow'
"""

__author__ = 'Bastien Gorissen'
__version__ = '0.1'
__email__ = ["kadomony@gmail.com"]

__bpydoc__ = """\
Usage: set parameters in the GUI and the script will analyze the
  exposure of target points over the set period of time
"""

import math
import time
import Blender
from Blender import *
from Blender.Scene import Render

scene = Scene.GetCurrent()
context = scene.getRenderingContext()

count = 0
for e in [obj for obj in scene.objects if obj.getType() == 'Empty']:
    count = count + 1
    camera = Camera.New('persp')
    cam = scene.objects.new(camera)
    scene.objects.camera = cam
    cam.setLocation(e.getLocation('worldspace'))
    context.imageType = Render.PNG
    context.imageSizeX(10)
    context.imageSizeY(10)
    context.render()
    context.saveRenderedImage('tmp' + str(count) + '.png')
    image = Image.Load(context.getRenderPath() + 'tmp' + str(count) + '.png')
    px_w = 0
    px_b = 0
    for x in range(image.getSize()[0]):
        for y in range(image.getSize()[1]):
            color = image.getPixelF(x,y)
            if (color[0]+color[1]+color[2])/3.0 > 0.5:
                px_w = px_w + 1
            else:
                px_b = px_b + 1

    print "There are " + str(px_w) + " white pixel, and " + str(px_b) + " black ones."

                
