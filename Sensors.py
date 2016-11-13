##### Sensor functionality

def getDistance(data):
    try: return data.distance #TEMPTEMPTEMP
    except: return 42

def changePosition(data): #called on every timerFired for Reps.py
            #Game.py should access getDistance() directly for finer control
    if (data.position == "Down"):
        if (data.distance <= data.upThreshold and data.distance != 0):
            data.position = "Up"
    elif (data.position == "Up"):
        if (data.distance >= data.upThreshold or data.distance == 0):
            data.position = "Down"