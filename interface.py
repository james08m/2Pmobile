import pygame
import datetime

# Main window class
class Win_Main:
    def __init__(self, screen):
        self.screen = screen
        self.open = True
        # Images  -----------------------------------------------
        self.IMG_Contacts = pygame.image.load("icons/contacts.png").convert()
        self.IMG_Settings = pygame.image.load("icons/settings.png").convert()
        self.IMG_Mail = pygame.image.load("icons/mail.png").convert()

        # Buttons -----------------------------------------------
        self.BTN_Contacts = Button((3,20,60,60))
        self.BTN_Contacts.setIcon(self.IMG_Contacts)

        self.BTN_Settings = Button((66,20,60,60))
        self.BTN_Settings.setIcon(self.IMG_Settings)

        self.BTN_Mail = Button((129,20,60,60))
        self.BTN_Mail.setIcon(self.IMG_Mail)

    def exect(self):
        while self.open:
            # Event handling
            event = pygame.event.poll()
            if event.type == pygame.MOUSEBUTTONDOWN: # If mouse down
                pos = pygame.mouse.get_pos()
            elif event.type == pygame.KEYDOWN: # If key down (not supose to happen)
                if event.key == pygame.K_ESCAPE:
                    self.open = False

            # Display components
            self.screen.fill((0,0,0))

            # Display header
            current_time = datetime.datetime.now().time() # Get time
            font = pygame.font.SysFont("verdana", 10)
            time_str = str(current_time.hour) + ":" + str(current_time.minute)
            time = font.render(time_str, 1, (255,255,255))
            self.screen.blit(time, (200, 3))

            # Display buttons
            self.BTN_Contacts.draw(self.screen)
            self.BTN_Settings.draw(self.screen)
            self.BTN_Mail.draw(self.screen)
            pygame.display.flip()



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

