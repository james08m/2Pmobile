import pygame
from utilities import *
from user import *


# Main window class
class WIN_Main:
    def __init__(self, screen, code):
        self.screen = screen
        self.open = True
        self.lastwindow = code

        # Images -----------------------------------------------
        #self.IMG_Background = pygame.image.load(User.getFilepath()+"/Pictures/bg.jpg")
        self.IMG_Background = pygame.image.load("/home/pi/Pictures/bg.jpg")
        self.IMG_Phone = pygame.image.load("icons/iphone.png")
        self.IMG_Messages = pygame.image.load("icons/imessages2.png")
        self.IMG_Music = pygame.image.load("icons/imusic.png")
        self.IMG_Contact = pygame.image.load("icons/icontact.png")
        self.IMG_Camera = pygame.image.load("icons/icamera.png")
        self.IMG_Video = pygame.image.load("icons/ivideo.png")

        # Header ------------------------------------------------
        self.Header = Header((0,0,20,240))

        # Buttons -----------------------------------------------
        self.BTN_Phone = Button((35,385,60,60))
        self.BTN_Phone.setIcon(self.IMG_Phone)

        self.BTN_Messages = Button((130,385,60,60))
        self.BTN_Messages.setIcon(self.IMG_Messages)

        self.BTN_Music = Button((225,385,60,60))
        self.BTN_Music.setIcon(self.IMG_Music)

        self.BTN_Contact = Button((35,295,60,60))
        self.BTN_Contact.setIcon(self.IMG_Contact)

        self.BTN_Camera = Button((130,295,60,60))
        self.BTN_Camera.setIcon(self.IMG_Camera)

        self.BTN_Video = Button((225,295,60,60))
        self.BTN_Video.setIcon(self.IMG_Video)

    def exect(self):
        while self.open:
            # Event handling
            event = pygame.event.poll()
            if event.type == pygame.MOUSEBUTTONDOWN: # If mouse down
                mouse_position = pygame.mouse.get_pos()
                if self.BTN_Phone.selected(mouse_position):
                    print "Phone"
                elif self.BTN_Messages.selected(mouse_position):
                    print "Messages"
                elif self.BTN_Music.selected(mouse_position):
                    print "Music"
                elif self.BTN_Contact.selected(mouse_position):
                    print "Contact"
                elif self.BTN_Camera.selected(mouse_position):
                    print "Camera"
                elif self.BTN_Video.selected(mouse_position):
                    print "Video"


            elif event.type == pygame.KEYDOWN: # If key down (not supose to happen)
                if event.key == pygame.K_ESCAPE:
                    self.open = False

            # Display background
            self.screen.blit(self.IMG_Background, (0,0))

            # Display header
            self.Header.draw(self.screen)


            # Display buttons
            self.BTN_Phone.draw(self.screen)
            self.BTN_Messages.draw(self.screen)
            self.BTN_Music.draw(self.screen)
            self.BTN_Contact.draw(self.screen)
            self.BTN_Camera.draw(self.screen)
            self.BTN_Video.draw(self.screen)
            pygame.display.flip()
        return 0



# Header class
class Header:
	def __init__(self, rect):
		self.rect = rect
		self.color = (0,0,0)
		self.font = pygame.font.SysFont("verdana", 13)

	def selected(self, pos):
		x1 = self.rect[0]
		y1 = self.rect[1]
		x2 = x1 + self.rect[2] - 1
		y2 = y1 + self.rect[3] - 1
		if ((pos[0] >= x1) and (pos[0] <= x2) and (pos[1] >= y1) and (pos[1] <= y2)):
			return True
		else:
			return False

	def draw(self, screen):
		
		# Display background in RGBA (Opacity)
		bg = pygame.Surface((self.rect[2], self.rect[3]))
		bg.set_alpha(128)
		bg.fill(self.color) 
		screen.blit(bg, self.rect)

		screen.fill(self.color, self.rect)
		screen.blit(self.font.render(User.getUsername(), 1, (255,255,255)), (275, 8))
		screen.blit(self.font.render(getTimeToMinutes(), 1, (255,255,255)), (10, 8))
		


# Button class
class Button:
    def __init__(self, rect):
        self.rect = rect
        self.color = None
        self.icon = None

    def selected(self, pos):
        x1 = self.rect[0]
        y1 = self.rect[1]
        x2 = x1 + self.rect[2] - 1
        y2 = y1 + self.rect[3] - 1
        if ((pos[0] >= x1) and (pos[0] <= x2) and (pos[1] >= y1) and (pos[1] <= y2)):
            return True
        else:
            return False

    def draw(self, screen):
        if self.icon:
            screen.blit(self.icon, self.rect)
        elif self.color:
            screen.fill(self.color, self.rect)

    def setIcon(self, image):
        self.icon = image

