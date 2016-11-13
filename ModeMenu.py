#####
# Mode Menu
#####

from Button import *
from Sensors import *
from tkinter import *
from PIL import Image, ImageTk

def initModeMenu(data):
    data.modeMenuBkgOpc = 0
    data.belhaech = 0
    data.greyBk = ImageButton(0, 0, img="temp.png")
    data.hangBtn = ImageCircleButton(105, 55, img="hang.png")
    data.repPullBtn = ImageCircleButton(205, 55, img="repPull.png")
    data.repPushBtn = ImageCircleButton(305, 55, img="repPush.png")
    data.gamePullBtn = ImageCircleButton(105, 155, img="gamePull.png")
    data.gamePushBtn = ImageCircleButton(205, 155, img="gamePush.png")
    data.customBtn = ImageCircleButton(305, 155, img="custom.png")

def modeMenuMousePressed(event, data, button):
    pass

def modeMenuTimerFired(data):
    pass

def modeMenuRedrawAll(canvas, data):
    if data.modeMenuActive and data.modeMenuBkgOpc<120:
        data.modeMenuBkgOpc += 30
        print(data.modeMenuBkgOpc, data.belhaech)
        bkg = Image.open('mainBkgrnd.png')
        bkgrnd = Image.new('RGBA', bkg.size)
        bkgrnd.paste(bkg)
        greyRect = Image.new('RGBA', bkg.size, (0,0,0,data.modeMenuBkgOpc))
        bkgrnd.paste(greyRect, box=(0,0), mask=greyRect)
        bkgrnd.save('temp.png', 'PNG')
    data.greyBk = ImageButton(0, 0, img="temp.png")
    data.greyBk.drawButton(canvas)
    if data.modeMenuBkgOpc >= 120:
        canvas.create_rectangle(60, 40, 420, 280, fill="white", width=0)
