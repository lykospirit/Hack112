#####
# Reps
#####

from Button import *
from Sensors import *

def initReps(data):
    data.reps = 0
    data.repsPos = "Down"
    data.repsOver = False

def repsMousePressed(event, data):
    data.mode = "main"
    initMain(data)

def repsTimerFired(data):
    if data.position != data.repsPos:
        if (data.repsPos == "Down"):
            data.reps += 1
            data.repsPos = data.position
        else:
            data.repsPos = data.position

def repsRedrawAll(canvas, data):
    drawReps(canvas, data)

def drawReps(canvas, data):
    canvas.create_rectangle(100, 80, 380, 200, fill="red")
    canvas.create_text(240, 140, text=str(data.reps),
                        font = "Helvetica 36 bold", fill="black")
    canvas.create_text(240, 30, text="Touch anywhere to end.", fill="blue",
                            font="Helvetica 16")




