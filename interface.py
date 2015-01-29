import pygame
from utilities import *


# Main window class
class Win_Main:
    def __init__(self, screen):
        self.screen = screen
        self.open = True
        # Images  -----------------------------------------------
        self.IMG_Video = pygame.image.load("icons/video.png")
        self.IMG_Music = pygame.image.load("icons/music.png")
        self.IMG_Camera = pygame.image.load("icons/camera.png")
        self.IMG_Messages = pygame.image.load("icons/messages.png")

        # Buttons -----------------------------------------------
        self.BTN_Video = Button((4,25,55,55))
        self.BTN_Video.setIcon(self.IMG_Video)

        self.BTN_Music = Button((63,25,55,55))
        self.BTN_Music.setIcon(self.IMG_Music)

        self.BTN_Camera = Button((122,25,55,55))
        self.BTN_Camera.setIcon(self.IMG_Camera)

        self.BTN_Messages = Button((181,25,55,55))
        self.BTN_Messages.setIcon(self.IMG_Messages)

    def exect(self):
        while self.open:
            # Event handling
            event = pygame.event.poll()
            if event.type == pygame.MOUSEBUTTONDOWN: # If mouse down
                mouse_position = pygame.mouse.get_pos()
                if self.BTN_Video.selected(mouse_position):
                    print("Video")
                elif self.BTN_Music.selected(mouse_position):
                    print("Music")
                elif self.BTN_Camera.selected(mouse_position):
                    print("Camera")
                elif self.BTN_Messages.selected(mouse_position):
                    print("Messages")


            elif event.type == pygame.KEYDOWN: # If key down (not supose to happen)
                if event.key == pygame.K_ESCAPE:
                    self.open = False

            # Display components
            self.screen.fill((0,0,0))

            # Display header
            font = pygame.font.SysFont("verdana", 10)
            time = font.render(getTimeToMinutes(), 1, (255,255,255))
            self.screen.blit(time, (200, 3))

            # Display buttons
            self.BTN_Video.draw(self.screen)
            self.BTN_Music.draw(self.screen)
            self.BTN_Camera.draw(self.screen)
            self.BTN_Messages.draw(self.screen)
            pygame.display.flip()
        return 0



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

