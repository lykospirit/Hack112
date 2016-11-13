#####
# Game
#####

from Button import *
from PIL import Image

def initGame(data):
    data.activeObstacles = []
    data.timeElapsed = 0
    data.remove = False
    data.obs = "low"
    data.player = Player()
    data.score = 0
    data.gameOver = False

def gameMousePressed(event, data):
    if (data.gameOver == False): pass
    else:
        data.mode = "main"
        initMain(data)

def gameTimerFired(data):
    if (data.gameOver == True): return
    data.timeElapsed += 1 #in twentieths of seconds approx.
    for obstacle in data.activeObstacles:
        obstacle.x -= 30
        if (obstacle.x < data.player.x and obstacle.type == "low"
                and obstacle.scored == False):
            data.score += 1
            obstacle.scored = True
        if obstacle.x < 0:
            data.remove = True
        if (data.player.isTouching(obstacle)):
            data.gameOver = True
    if data.timeElapsed%7 == 0:
        newObstacle = Obstacle(data.obs, data)
        data.activeObstacles.append(newObstacle)
        if (data.obs) == "low": data.obs = "high"
        elif (data.obs) == "high": data.obs = "low"
    if data.remove == True:
        data.activeObstacles.pop(0)
        data.remove = False
    data.player.movePlayer(data)

def gameRedrawAll(canvas, data):
    for obstacle in data.activeObstacles:
        obstacle.drawObstacle(canvas)
    data.player.drawPlayer(canvas)
    drawScore(canvas, data)
    if (data.gameOver == True):
            drawGameOver(canvas, data)

def drawGameOver(canvas, data):
    canvas.create_rectangle(40, 100, 440, 220, fill="black")
    canvas.create_text(240, 130, text="Game Over. Score: %d" % data.score,
                                                fill="cyan", font="Helvetica 20 bold")
    canvas.create_text(240, 190, text="Touch anywhere to go back to the main menu.",
                                                fill="cyan", font="Helvetica 14")

def drawScore(canvas, data):
    canvas.create_rectangle(20, 20, 80, 80, fill="black")
    canvas.create_text(50, 50, text="%d" % data.score, font="Helvetica 24",
                            fill = "green")

class Obstacle(object):
    def __init__(self, obsType, data, screenWidth=480, screenHeight=280):
        self.w = screenWidth
        self.h = screenHeight
        self.type = obsType
        self.x = self.w
        self.img = data.obstacleImage
        self.scored = False

    def drawObstacle(self, canvas):
        if self.type == "low":
            canvas.create_image(self.x, self.h/2, anchor=NW, image=self.img)
        elif self.type == "high":
            canvas.create_image(self.x, 0, anchor=NW, image=self.img)

    def getBounds(self):
        if self.type == "low":
            return (self.x, self.h/2, self.x+25, self.h)
        else:
            return (self.x, 0, self.x+25, self.h/2)

class Player(object):
    def __init__(self):
        self.h = 280
        self.x = 240
        self.y = 3*self.h//4
        self.lowest = 3*self.h//4
        self.highest = self.h//4
        self.difference = self.lowest - self.highest
        self.width = 16
        self.height = 30
        self.right = self.x + self.width / 2
        self.left = self.x - self.width /2
        self.top = self.y - self.height / 2
        self.bot = self.y + self.height / 2

    def updateBounds(self):
        self.right = self.x + self.width / 2
        self.left = self.x - self.width /2
        self.top = self.y - self.height / 2
        self.bot = self.y + self.height / 2

    def drawPlayer(self, canvas):
        player = ImageCircleButton(self.x-8, self.y-15, img="kosbie.png")
        player.drawButton(canvas)
        # canvas.create_oval(self.x-8, self.y-15, self.x+8, self.y+15, fill="cyan")

    def movePlayer(self, data):
        if (data.position == "Up"):
            if (self.y > self.highest):
                self.y -= 40
            if (self.y < self.highest):
                self.y = self.highest
        elif (data.position == "Down"):
            if (self.y < self.lowest):
                self.y += 40
            if (self.y > self.lowest):
                self.y = self.lowest
        self.updateBounds()

    def isTouching(self, other):
        if ((self.right > (other.getBounds()[0]+2) and self.right < (other.getBounds()[2]-2)) or (self.left > (other.getBounds()[0]+2) and self.left < (other.getBounds()[2]-2))):
            if ((self.top > (other.getBounds()[1]+2) and self.top < (other.getBounds()[3]-2)) or (self.bot > (other.getBounds()[1]+2) and self.bot < (other.getBounds()[3]-2))):
                return True
        else:
            return False
