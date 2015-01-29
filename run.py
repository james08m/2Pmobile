# Import
import pygame
import os
from user import *
from log import *
from interface import *
from utilities import *

# Initialization ----------------------------------------
log = Log()
log.load()
log.add("boot...")
log.add("Loading user...")
user = User()
user.load()
user.lastlogin = getTimeToMinutes()

log.add("Init framebuffer/touchscreen and environment variables...")
# Init framebuffer/touchscreen environment variables     # Code from piPhone github
#os.putenv('SDL_VIDEODRIVER', 'fbcon')
#os.putenv('SDL_FBDEV'      , '/dev/fb1')
#os.putenv('SDL_MOUSEDRV'   , 'TSLIB')
#os.putenv('SDL_MOUSEDEV'   , '/dev/input/touchscreen')

log.add("Hidding mouse cursor...")
#pygame.mouse.set_visible(False)

log.add("Init screen display...")
pygame.init()
window  = pygame.display.set_mode((240,320))

# Mainloop ----------------------------------------------
log.add("Luching...")
WIN_Main = Win_Main(window)
WIN_Main.exect()

log.add("Saving user..")
user.save()
log.add("Quit")

log.save()