#####
# Workout Mode
#####

from Button import *
from Game import *
from Reps import *
from Hang import *

def initWorkout(data):
    pass

def workoutMousePressed(event, data, button):
    if (data.workoutMode == "gamePull" or data.workoutMode == "gamePush"): gameMousePressed(event, data)
    elif (data.workoutMode == "repPull" or data.workoutMode == "repPush"): repsMousePressed(event, data)
    elif (data.workoutMode == "hang"): hangMousePressed(event, data)

def workoutTimerFired(data):
    changePosition(data)
    if (data.workoutMode == "gamePull" or data.workoutMode == "gamePush"): gameTimerFired(data)
    elif (data.workoutMode == "repPull" or data.workoutMode == "repPush"): repsTimerFired(data)
    elif (data.workoutMode == "hang"): hangTimerFired(data)

def workoutRedrawAll(canvas, data):
    if (data.workoutMode == "gamePull" or data.workoutMode == "gamePush"): gameRedrawAll(canvas, data)
    elif (data.workoutMode == "repPull" or data.workoutMode == "repPush"): repsRedrawAll(canvas, data)
    elif (data.workoutMode == "hang"): hangRedrawAll(canvas, data)
