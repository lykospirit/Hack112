#####
# Main
#####

from Button import *
from MainMenu import *
from ModeMenu import *
from Game import *
from Hang import *
from Reps import *

def initMain(data):
    startButtonRad = 110
    startButtonCx = 240
    startButtonCy = 140
    modeButtonRad = 35
    modeButtonCx = 360
    modeButtonCy = 200
    modeButtonImg = "%s.png" % data.workoutMode
    data.startButton = ImageCircleButton(startButtonCx-startButtonRad, startButtonCy-startButtonRad,
                                                    name="Start", img="playIcon.png")
    data.modeButton = ImageCircleButton(modeButtonCx-modeButtonRad, modeButtonCy-modeButtonRad,
                                                    name="Mode", img=modeButtonImg)
    data.openMenuButton = ImageButton(0, 0, name="Menu", img="menuIcon.png")

    data.activeButtons = []
    data.activeButtons.append(data.startButton)
    data.activeButtons.append(data.modeButton)
    data.activeButtons.append(data.openMenuButton)

def mainMousePressed(event, data, button):
    if button.name == 'Menu':
        initMainMenu(data)
        data.mainMenuActive = True
    elif button.name == 'Mode':
        initModeMenu(data)
        data.modeMenuActive = True
    elif button.name == 'Start':
        data.mode = 'workout'
        if data.workoutMode == "gamePull" or data.workoutMode == "gamePush": initGame(data)
        elif data.workoutMode == "repPull" or data.workoutMode == "repPush": initReps(data)
        elif data.workoutMode == "hang": initHang(data)

def mainTimerFired(data):
    pass

def mainRedrawAll(canvas, data):
    data.openMenuButton.drawButton(canvas)
    data.startButton.drawButton(canvas)
    data.modeButton.drawButton(canvas)
