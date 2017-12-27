from Squizzard.Drawable import Drawable
from Squizzard.ExistenceState import ExistenceState

#Defines base mob behavior -- everything that can move is a decendent of this class
class Mob(Drawable):
    def __init__(self, x = 0, y = 0):
        Drawable.__init__(self, x, y)
        self.x = x
        self.y = y

        self.state = ExistenceState.ACTIVE

        return

    def move(self):
        pass

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state
        return

    def logic(self):
        pass
