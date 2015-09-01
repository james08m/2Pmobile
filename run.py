# Import
import pygame
import os
#from user import *
#from log import *
from interface import *
from utilities import *

# Initialization ----------------------------------------
#log = Log()
#log.load()
#log.add("["+ getTimeToSecondes() + "] booting...")
#log.add("Loading user...")

#log.add("Init framebuffer/touchscreen and environment variables...")
# Init framebuffer/touchscreen environment variables     # Code from piPhone github
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV'      , '/dev/fb1')
os.putenv('SDL_MOUSEDRV'   , 'TSLIB')
os.putenv('SDL_MOUSEDEV'   , '/dev/input/touchscreen')


#log.add("Init screen display...")
pygame.init()
pygame.mouse.set_visible(False)
screen  = pygame.display.set_mode((320,480))

# Mainloop ----------------------------------------------
#log.add("Lunching...")
window = WIN_Main(screen, 0)
window.exect()

#log.add("Saving user..")
#log.add("Quit")

#log.save()
