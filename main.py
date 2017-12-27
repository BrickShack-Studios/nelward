import pygame
from random import randrange

import Squizzard

#Starts PyGame so that its functions can be used
pygame.init()

#Global variables (don't do this I'm a bad boy)
windowSize = (160, 144)
backgroundColor = (0, 0, 240)
foregroundColor = (221, 130, 129)

#screen is the variable we'll use to hold an object of a Screen class.
#A Screen object holds all of the data for a window. Things like its
#size, its name, whether the mouse appears on it or not, etc
#The Screen is also where the actual pixel data gets drawn to so that
#there's something to see.
#Here, we initialize it to a None type, because we're about to set it
#to an actual screen, depending on whether or not we want the game
#to be fullscreen. We want fullscreen for the final game, but
#windowed while developing it. That's because if it crashes in
#fullscreen we've borked it (on Linux at least).
screen = None

FULLSCREEN = 0
if (FULLSCREEN == 1):
    #Creates a fullscreen Screen and saved it to screen
    screen = pygame.display.set_mode(windowSize, pygame.FULLSCREEN)
else:
    #Creates a windowed Screen and saves it to screen
    screen = pygame.display.set_mode(windowSize)

#Sets the name of the window
pygame.display.set_caption("Nelward the Squizzard")

#Hides the mouse
pygame.mouse.set_visible(False)

#Initializes a clock for locking fps
clock = pygame.time.Clock()


#=======================================================================

#Checks if the X button was pressed
def quitLoop(events):
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    return

#Checks if the escape key way pressed
def parseInputs(keys):
    if (keys[pygame.K_ESCAPE] == 1):
        pygame.quit()
        quit()
    return

#Checks all entities in the list to see is they need to be destroyed
#If they do, add them to a separate list
#Iterates over this list to remove its elements from the main entity list,
#effectively destroying them
def collectGarbage(mobs):
    garbage = []
    for m in mobs:
        if m.getState() == Squizzard.ExistenceState.ExistenceState.DESTROY:
            garbage.append(m)

    for g in garbage:
        mobs.remove(g)

    return


#=======================================================================

#The player is Nelward
player = Squizzard.Nelward.Nelward(windowSize)
#Used to store mobs
mobs = []

while (True):
    #tick() is used to cap fps at 60
    clock.tick(60)
    #Wipes screen for redrawing
    screen.fill(backgroundColor)

    #Collects keys pressed at this moment
    keys = pygame.key.get_pressed()

    #Checks if the game needs to be closed
    quitLoop(pygame.event.get())
    parseInputs(keys)

    #Handles player movement/drawing
    player.move(keys)
    player.draw(screen)

    #Handles spawning
    if (randrange(0, 60) == 0):
        mobs.append(Squizzard.Pickups.Food(windowSize))

    if (randrange(0, 120) == 0):
        mobs.append(Squizzard.Enemies.Net(windowSize))

    if (randrange(0, 480) == 0):
        mobs.append(Squizzard.Enemies.Predator(windowSize))

    #Calls garbage collector. If performance is an issue, call
    #every 2 frames, or every 3, etc
    collectGarbage(mobs)

    #Handles all mob logic/drawing
    for m in mobs:
        m.logic()
        m.draw(screen)

    #Updates the screen
    pygame.display.flip()
