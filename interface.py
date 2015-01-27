import pygame

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

