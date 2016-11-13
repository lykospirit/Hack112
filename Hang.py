#####
# Hang
#####

from Button import *
from Sensors import *
import time

def initHang(data):
    data.startTime = time.time()
    data.hangTime = 10
    data.hangTimeColor = "white"

def hangMousePressed(event, data):
    pass

def hangTimerFired(data):
    now = time.time()
    if (now - data.startTime >= 1):
        if (data.hangTime != 0):
            data.hangTime -= 1
            data.startTime = now
        else:
            if (data.hangTimeColor == "white"): data.hangTimeColor = "red"
            else: data.hangTimeColor = "white"
            data.startTime = now

def hangRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, 480, 320, fill="navyblue")
    drawTime(canvas, data)

def drawTime(canvas, data):
    canvas.create_oval(180, 100, 300, 220, fill="black")
    canvas.create_text(240, 160, text="%d" % data.hangTime,
                        font="Helvetica 40 bold", fill=data.hangTimeColor)


