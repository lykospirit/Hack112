#####
# Workout Mode
#####

from Button import *
from Game import *
from Reps import *
from Hang import *
from Sensors import *

def initWorkout(data):
    data.workoutMode = "game"
    initGame(data)

def workoutMousePressed(event, data):
    if (data.workoutMode == "game"): gameMousePressed(event, data)
    elif (data.workoutMode == "reps"): repsMousePressed(event, data)
    elif (data.workoutMose == "hang"): hangMousePressed(event, data)

def workoutTimerFired(data):
    changePosition(data)
    if (data.workoutMode == "game"): gameTimerFired(data)
    elif (data.workoutMode == "reps"): repsTimerFired(data)
    elif (data.workoutMode == "hang"): hangTimerFired(data)

def workoutRedrawAll(canvas, data):
    if (data.workoutMode == "game"): gameRedrawAll(canvas, data)
    elif (data.workoutMode == "reps"): repsRedrawAll(canvas, data)
    elif (data.workoutMode == "hang"): hangRedrawAll(canvas, data)
