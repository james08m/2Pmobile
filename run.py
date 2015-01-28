# Import
import pygame
import os
from user import *
from log import *
from interface import *

# Initialization ----------------------------------------
print("Initialization...")
log = Log()
log.load()

log.add("Loading user...")
user = User()
user.load()

log.add("Init framebuffer/touchscreen and environment variables...")
# Init framebuffer/touchscreen environment variables     # Code from piPhone github
#os.putenv('SDL_VIDEODRIVER', 'fbcon')
#os.putenv('SDL_FBDEV'      , '/dev/fb1')
#os.putenv('SDL_MOUSEDRV'   , 'TSLIB')
#os.putenv('SDL_MOUSEDEV'   , '/dev/input/touchscreen')

log.add("Hidding mouse...")
#pygame.mouse.set_visible(False)

log.add("Set display...")
pygame.init()
window  = pygame.display.set_mode((240,320))

# Mainloop ----------------------------------------------
log.add("Main window...")
WIN_Main = Win_Main(window)
WIN_Main.exect()

log.add("Quit")
