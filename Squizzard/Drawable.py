from Squizzard.Entity import Entity

#Defines the base draw() function -- everything that can appear on screen
#is a decendent of this class
class Drawable(Entity):
    def __init__(self, x = 0, y = 0):
        Entity.__init__(self, x, y)

        return

    def draw(self, screen):
        global foregroundColor

        pygame.draw.rect(screen, foregroundColor, (self.x, self.y, 10, 10), 0)

        return
