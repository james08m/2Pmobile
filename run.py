# Import
import pygame
import os
from user import *
from interface import *
import datetime

# Initialization ----------------------------------------
print("Initialization...")

print("Loading user...")
user = User()
user.load()
print("Hi " + user.username)
print("Last login at " + user.lastlogin) 

print("Init framebuffer/touchscreen and environment variables...")
# Init framebuffer/touchscreen environment variables     # Code from piPhone github
#os.putenv('SDL_VIDEODRIVER', 'fbcon')
#os.putenv('SDL_FBDEV'      , '/dev/fb1')
#os.putenv('SDL_MOUSEDRV'   , 'TSLIB')
#os.putenv('SDL_MOUSEDEV'   , '/dev/input/touchscreen')

print("Hidding mouse...")
#pygame.mouse.set_visible(False)

print("Set display...")
pygame.init()
window  = pygame.display.set_mode((240,320))

# Buttons -----------------------------------------------
img_btn1 = pygame.image.load("icons/contacts.png").convert()
button1 = Button((3,20,60,60))
button1.setIcon(img_btn1)

img_btn2 = pygame.image.load("icons/settings.png").convert()
button2 = Button((66,20,60,60))
button2.setIcon(img_btn2)

img_btn3 = pygame.image.load("icons/mail.png").convert()
button3 = Button((129,20,60,60))
button3.setIcon(img_btn3)

# Images ------------------------------------------------
img_bg = pygame.image.load("images/bg.jpg").convert()

# Mainloop ----------------------------------------------
print("Mainloop...")
Running = True
while Running:
	event = pygame.event.poll()
	if event.type == pygame.MOUSEBUTTONDOWN:
		pos = pygame.mouse.get_pos() # Get mouse position if touch
	elif event.type == pygame.KEYDOWN:
		if event.key == pygame.K_ESCAPE:
			Running = False
	
	# Set black background
	window.fill((0,0,0))
	
	# Display header
	current_time = datetime.datetime.now().time() # Get time
	font = pygame.font.SysFont("verdana", 10)
	time_str = str(current_time.hour) + ":" + str(current_time.minute)
	time = font.render(time_str, 1, (255,255,255))
	window.blit(time, (200, 3))
	
	
	# Display buttons
	button1.draw(window)
	button2.draw(window)
	button3.draw(window)
	pygame.display.flip()

print("Quit")
