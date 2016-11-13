#####
# Mode Menu
#####

from Button import *
from tkinter import *
from PIL import Image
from Main import *

def initModeMenu(data):
    data.modeMenuBkgOpc = 0
    data.greyBk = ImageButton(0, 0, img="temp.png")
    data.hangBtn = ImageCircleButton(105, 55, img="hang.png", name="hang", parent="ModeMenu")
    data.repPullBtn = ImageCircleButton(205, 55, img="repPull.png", name="repPull", parent="ModeMenu")
    data.repPushBtn = ImageCircleButton(305, 55, img="repPush.png", name="repPush", parent="ModeMenu")
    data.gamePullBtn = ImageCircleButton(105, 155, img="gamePull.png", name="gamePull", parent="ModeMenu")
    data.gamePushBtn = ImageCircleButton(205, 155, img="gamePush.png", name="gamePush", parent="ModeMenu")
    data.customBtn = ImageCircleButton(305, 155, img="custom.png", name="custom", parent="ModeMenu")

    data.activeButtons = []
    data.activeButtons.append(data.greyBk)
    data.activeButtons.append(data.hangBtn)
    data.activeButtons.append(data.repPullBtn)
    data.activeButtons.append(data.repPushBtn)
    data.activeButtons.append(data.gamePullBtn)
    data.activeButtons.append(data.gamePushBtn)
    data.activeButtons.append(data.customBtn)

def modeMenuMousePressed(event, data, button):
    if button.name == "hang": data.workoutMode = 'hang'
    elif button.name == "repPull": data.workoutMode = 'repPull'
    elif button.name == "repPush": data.workoutMode = 'repPush'
    elif button.name == "gamePull": data.workoutMode = 'gamePull'
    elif button.name == "gamePush": data.workoutMode = 'gamePush'
    elif button.name == "custom": data.workoutMode = 'custom'
    data.modeMenuActive = False

def modeMenuTimerFired(data):
    pass

def modeMenuRedrawAll(canvas, data):
    if (data.modeMenuActive and data.modeMenuBkgOpc<120) or (not data.modeMenuActive and data.modeMenuBkgOpc>0):
        if data.modeMenuActive and data.modeMenuBkgOpc<120:
            data.modeMenuBkgOpc += 30
        else: data.modeMenuBkgOpc -= 30
        bkg = Image.open('mainBkgrnd.png')
        bkgrnd = Image.new('RGBA', bkg.size)
        bkgrnd.paste(bkg)
        greyRect = Image.new('RGBA', bkg.size, (0,0,0,data.modeMenuBkgOpc))
        bkgrnd.paste(greyRect, box=(0,0), mask=greyRect)
        bkgrnd.save('temp.png', 'PNG')
    data.greyBk = ImageButton(0, 0, img="temp.png")
    data.greyBk.drawButton(canvas)
    if data.modeMenuBkgOpc >= 120:
        canvas.create_rectangle(90, 40, 390, 240, fill="white", width=0)
        data.hangBtn.drawButton(canvas)
        data.repPullBtn.drawButton(canvas)
        data.repPushBtn.drawButton(canvas)
        data.gamePullBtn.drawButton(canvas)
        data.gamePushBtn.drawButton(canvas)
        data.customBtn.drawButton(canvas)
