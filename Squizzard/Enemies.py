from Squizzard.Mob import Mob
from Squizzard.Sprite import Sprite
from Squizzard.ExistenceState import ExistenceState

from random import randrange

#The predator enemy class
class Predator(Mob):
    def __init__(self, windowSize, x = 0, y = 0):
        Mob.__init__(self, x, y)

        self.windowSize = windowSize
        self.sprite = Sprite("Squizzard/sprites/shark.png")
        self.sprite.setSize(2)
        self.size = self.sprite.getSize()[0]
        self.speed = 3

        self.state = ExistenceState.ACTIVE

        if (self.x == 0 and self.y == 0):
            self.x = randrange(0, self.windowSize[0])
            self.y = -self.size

        return

    def move(self):
        self.y += self.speed

        if (self.y > self.windowSize[1] + self.size):
            self.state = ExistenceState.DESTROY

        return

    def logic(self):
        self.move()
        return

    def getState(self):
        return self.state

    def draw(self, screen):
        self.sprite.draw(screen, int(self.x), int(self.y))
        return

#The net enemy class
class Net(Mob):
    def __init__(self, windowSize, x = 0, y = 0):
        Mob.__init__(self, x, y)

        self.windowSize = windowSize
        self.speed = 2
        self.sprite = Sprite("Squizzard/sprites/net.png")
        self.size = self.sprite.getSize()[0]

        if (self.x == 0 and self.y == 0):
            self.x = randrange(0, int(self.windowSize[1] - self.size / 2))
            self.y = -self.size

        return

    def move(self):
        self.y += self.speed

        if (self.y > self.windowSize[1]):
            self.state = ExistenceState.DESTROY

        return

    def logic(self):
        self.move()

        return

    def draw(self, screen):
        self.sprite.draw(screen, int(self.x), int(self.y))
        return

    def getState(self):
        return self.state
