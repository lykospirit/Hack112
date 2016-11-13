##### Sensor functionality

#def getDistance():
#    try: return 42 #TEMPTEMPTEMP
#    except: return 42

import serial
import time

try:
    ser = serial.Serial('/dev/ttyACM0',9600)
except:
    ser = serial.Serial('/dev/ttyACM1',9600)

def getDistance():
    serialInput = ser.readline()
    try:
        serialInput = serialInput.decode("ascii")
        output = ""
        for c in serialInput:
            if c.isdigit():
                output += c
        output = int(serialInput)
        return(output)
    except:
        return 0


def changePosition(data): #called on every timerFired for Reps.py
            #Game.py should access getDistance() directly for finer control
    if (data.position == "Down"):
        if (data.distance <= data.upThreshold and data.distance != 0):
            data.position = "Up"
    elif (data.position == "Up"):
        if (data.distance >= data.upThreshold or data.distance == 0):
            data.position = "Down"
