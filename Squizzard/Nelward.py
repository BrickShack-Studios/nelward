import pygame
from Squizzard.Mob import Mob
from Squizzard.Sprite import Sprite

#Defines the main player class
class Nelward(Mob):
    def __init__(self, windowSize, x = -1, y = -1):
        self.windowSize = windowSize
        if (x == -1 and y == -1):
            x = int(self.windowSize[0] / 2)

        Mob.__init__(self, x, y)
        self.x = x
        self.y = y

        self.maxSpeed = 1.5
        self.speed = 0

        self.sprite = Sprite("Squizzard/sprites/nelward.png")
        self.sprite.setSize(2)
        self.size = self.sprite.getSize()[0]

        self.drag = 10

        #If he was spawned at the default starting spot,
        #place him in the center of the screen, 3/4ths of the way
        #down
        if (self.y == -1):
            self.y = self.windowSize[1] / 4 * 3 - int(self.size / 2)

        return

    def move(self, keys):
        global windowSize

        #If D is pressed and Nelward isn't going to go offscreen to the right
        #and his speed is <= the max speed, then increase his rightward momentum
        if (keys[pygame.K_d] == 1 and self.x + self.size < self.windowSize[0] and
            (self.speed + self.maxSpeed / self.drag) <= self.maxSpeed):

            self.speed += self.maxSpeed / self.drag

        #If A is pressed and Nelward isn't going to go offscreen to the left
        #and his speed is >= -maxSpeed, then increase his leftward momentum
        elif (keys[pygame.K_a] == 1 and self.x > 0 and
              (self.speed - self.maxSpeed / self.drag) >= -self.maxSpeed):

            self.speed -= self.maxSpeed / self.drag

        #If nothing is pressed, slow him down until we're close enough to
        #a speed of 0 to snap to 0, thereby stopping him
        else:
            if (abs(self.speed) <= self.maxSpeed / self.drag):
                self.speed = 0
            elif (self.speed > 0):
                self.speed -= self.maxSpeed / self.drag
            elif (self.speed < 0):
                self.speed += self.maxSpeed / self.drag

        #If he touches the left or right bounds of the screen, stop him
        if (self.x + self.size + self.speed > self.windowSize[0] or self.x + self.speed < 0):
            self.speed = 0


        self.x += self.speed

        return


    def draw(self, screen):
        self.sprite.draw(screen, int(self.x), int(self.y))

        return
