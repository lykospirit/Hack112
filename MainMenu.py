#####
# Main Menu
#####

from Button import *
from Sensors import *

def initMainMenu(data):
    pass
    
def mainMenuMousePressed(event, data):
    if (data.workoutButton.isPressed(event.x, event.y)):
            data.mode = "workout"
    elif (data.gameButton.isPressed(event.x, event.y)):
            data.mode = "game"

def mainMenuTimerFired(data):
    pass

def mainMenuRedrawAll(canvas, data):
    data.workoutButton.drawButton(canvas)
    data.gameButton.drawButton(canvas)