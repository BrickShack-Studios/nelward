import pygame
from Squizzard.Drawable import Drawable

#Defines how base Sprites should work
class Sprite(Drawable):
    def __init__(self, imagePath):
        Drawable.__init__(self)

        #Loads an image, keeping transparency
        self.image = pygame.image.load(imagePath).convert_alpha()

        return

    def getSize(self):
        return self.image.get_rect().size

    #Multiplies the size of an image by factor. 2 is doubling the image, 1/2 is halving it.
    def setSize(self, factor):
        self.image = pygame.transform.scale(self.image, (int(self.getSize()[0] * factor), int(self.getSize()[1] * factor)))
        return

    def draw(self, screen, x = 0, y = 0):
        screen.blit(self.image, (x, y))
        return
