#####
# Game
#####

from Button import *

def initGame(data):
    data.activeObstacles = []
    data.timeElapsed = 0
    data.remove = False
    data.obs = "low"

def gameMousePressed(event, data):
    pass

def gameTimerFired(data):
    data.timeElapsed += 1 #in tenths of seconds
    for obstacle in data.activeObstacles:
        obstacle.x -= 10
        if obstacle.x < 0:
            data.remove = True
    if data.timeElapsed%12 == 0:
        newObstacle = Obstacle(data.obs)
        data.activeObstacles.append(newObstacle)
        if (data.obs) == "low": data.obs = "high"
        elif (data.obs) == "high": data.obs = "low"
    if data.remove == True:
        data.activeObstacles.pop(0)
        data.remove = False

def gameRedrawAll(canvas, data):
    for obstacle in data.activeObstacles:
        obstacle.drawObstacle(canvas)

class Obstacle(object):
    def __init__(self, obsType, screenWidth=480, screenHeight=320):
        self.w = screenWidth
        self.h = screenHeight
        self.type = obsType
        self.x = self.w
    
    def drawObstacle(self, canvas):
        if self.type == "low":
            canvas.create_rectangle(self.x, self.h/2, self.x + 25,
                                    self.h, fill="red")
        elif self.type == "high":
            canvas.create_rectangle(self.x, 0, self.x + 25, self.h/2,
                                        fill="red")
    
    