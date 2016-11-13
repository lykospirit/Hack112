#####
# Main
#####

from Button import *

def initMain(data):
    startButtonRad = 120
    startButtonCx = 240
    startButtonCy = 160
    modeButtonRad = 55
    modeButtonCx = 360
    modeButtonCy = 240
    data.startButton = CircleButton(startButtonCx-startButtonRad, startButtonCy-startButtonRad,
        startButtonCx+startButtonRad, startButtonCy+startButtonRad, name="Start", color="#06a8ac")
    data.modeButton = CircleButton(modeButtonCx-modeButtonRad, modeButtonCy-modeButtonRad,
        modeButtonCx+modeButtonRad, modeButtonCy+modeButtonRad, name="Mode", color="#f46e15")
    data.openMenuButton = ImageButton(0, 0, name="Menu", img="menuIcon.png")

    data.activeButtons.append(data.startButton)
    data.activeButtons.append(data.modeButton)
    data.activeButtons.append(data.openMenuButton)

def mainMousePressed(event, data):
    pass

def mainTimerFired(data):
    pass

def mainRedrawAll(canvas, data):
    data.openMenuButton.drawButton(canvas)
    data.startButton.drawButton(canvas)
    data.modeButton.drawButton(canvas)
