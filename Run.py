##### Hack112--Pull-Up Procrastinators
# Matthew Spettel, Colin Gay, Kyle Jannak-Huang, Ryan Jannak-Huang
#####

from tkinter import *
from Button import *
from Main import *
from Workout import *
from ModeMenu import *
from MainMenu import *
from Sensors import *
from PIL import Image
import time

#####
# Run App
#####

def keyPressed(event, data): #TEMPTEMPTEMPTEMP
    if (event.keysym == "Up"):
        data.distance -= 10
    elif (event.keysym == "Down"):
        data.distance += 10

def timerFired(data):
    data.distance = getDistance()
    if data.mode == "workout": workoutTimerFired(data)

def init(data):
    data.mode = "main"
    data.activeButtons = []
    data.mainMenuActive = False
    data.modeMenuActive = False
    data.mode = "main"
    data.workoutMode = "hang"
    data.backgroundColor = "#f9feff"
    data.time = time.time()

    data.upThreshold = 25
    data.position = "Down"
    data.distance = getDistance()

    data.obstacleImage = PhotoImage(file="Obstacles.png")
    label = Label(image=data.obstacleImage)
    label.image = data.obstacleImage

    initMain(data)
    initWorkout(data)



def mousePressed(event, data):
    print(len(data.activeButtons))
    for button in range(len(data.activeButtons)-1, -1, -1):
        if data.activeButtons[button].isPressed(event.x, event.y):
            print(data.activeButtons[button].name)
            if data.mode == "main":
                if data.activeButtons[button].parent == "ModeMenu":
                    modeMenuMousePressed(event, data, data.activeButtons[button])
                    initMain(data)
                elif data.activeButtons[button].parent == "MainMenu":
                    mainMenuMousePressed(event, data, data.activeButtons[button])
                    initMain(data)
                else:
                    mainMousePressed(event, data, data.activeButtons[button])
            elif data.mode == "workout":
                workoutMousePressed(event, data, data.activeButtons[button])
            break

def redrawAll(canvas, data):
    if (data.mode == "main"):
        if (data.modeMenuActive == True):
            modeMenuRedrawAll(canvas, data)
        elif (data.mainMenuActive == True):
            mainMenuRedrawAll(canvas, data)
        else:
            canvas.create_rectangle(-5, -5, data.width+5, data.height+5, fill=data.backgroundColor, width=0)
            mainRedrawAll(canvas, data)
    elif (data.mode == "workout"): workoutRedrawAll(canvas, data)

### run function, as used in the CMU 15-112 course. Credit: David Kosbie
def run(width=480, height=280):
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
        # while True:
        #     if time.time() - data.time > 0:
        timerFired(data)
        redrawAllWrapper(canvas, data)
        #         data.time = time.time()
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)


    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 10 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
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
