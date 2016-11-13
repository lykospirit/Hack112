#####
# Main
#####

from Button import *

def initMain(data):
    data.startButton = Button(data.width/10, data.height/2,
        data.width*2/5, data.height*9/10, "Start")
    data.modeButton = Button(data.width*3/5, data.height/2,
        data.width*9/10, data.height*9/10, "Mode")
    data.openMenuButton = Button(0, 0, 50, 50)

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
