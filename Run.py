##### Hack112--Pull-Up Procrastinators
# Matthew Spettel, Colin Gay, Kyle Jannak-Huang, Ryan Jannak-Huang
#####

from tkinter import *
from Button import *
from Main import *
from Workout import *
from ModeMenu import *
from MainMenu import *

#####
# Run App
#####

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def init(data):
    data.mode = "main"
    data.activeButtons = []
    data.mainMenuActive = False
    data.modeMenuActive = False

    initMain(data)
    data.mode = "workout" # TEMPTEMPTEMPTEMPTEMPTEMP

def mousePressed(event, data):
    for button in range(0, len(data.activeButtons), -1):
        if data.activeButtons[button].isPressed(event.x, event.y):
            if data.mode == "main":
                if data.activeButtons[button].parent == "ModeMenu":
                    modeMenuMousePressed(event, data)
                elif data.activeButtons[button].parent == "MainMenu":
                    mainMenuMousePressed(event, data)
                else:
                    mainMousePressed(event, data)
            elif data.mode == "workout":
                workoutMousePressed(event, data)
            break

def redrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="white")
    if (data.mode == "main"):
        mainRedrawAll(canvas, data)
        if (data.modeMenuActive == True):
            modeMenuRedrawAll(canvas, data)
        elif (data.mainMenuActive == True):
            mainMenuRedrawAll(canvas, data)
    elif (data.mode == "workout"): workoutRedrawAll(canvas, data)

### run function, as used in the CMU 15-112 course. Credit: David Kosbie
def run(width=480, height=320):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    root.wm_title("Workout Game")
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")


run()
