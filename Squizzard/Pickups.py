from Squizzard.Mob import Mob
from Squizzard.Sprite import Sprite
from Squizzard.ExistenceState import ExistenceState
from random import randrange

#The food pickup
class Food(Mob):
    def __init__(self, windowSize, x = 0, y = 0):
        Mob.__init__(self)
        self.windowSize = windowSize
        self.x = x
        self.y = y
        self.speed = 1

        self.sprite = Sprite("Squizzard/sprites/food.png")
        self.size = self.sprite.getSize()[0]

        #If the food was at (0, 0), then place it
        #randomly at the top of the screen
        if (self.x == 0 and self.y == 0):
            self.x = randrange(0, int(self.windowSize[1] - self.size / 2))
            self.y = -self.size

        return

    def draw(self, screen):
        self.sprite.draw(screen, int(self.x), int(self.y))
        return

    def move(self):
        self.y += self.speed

        return

    def logic(self):
        if (self.y > self.windowSize[1]):
            self.state = ExistenceState.DESTROY
        else:
            self.move()

        return
