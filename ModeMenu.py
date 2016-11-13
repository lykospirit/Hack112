#####
# Mode Menu
#####

from Button import *
from Sensors import *
from tkinter import *
# from PIL import Image, ImageTk

def initModeMenu(data):
    data.modeMenuBkgOpc = 0
    data.belhaech = 0

def modeMenuMousePressed(event, data, button):
    pass

def modeMenuTimerFired(data):
    pass

def modeMenuRedrawAll(canvas, data):
    # if data.modeMenuActive and data.modeMenuBkgOpc<120:
    #     data.modeMenuBkgOpc += 20
    #     print(data.modeMenuBkgOpc, data.belhaech)
    #     bkg = Image.open('mainBkgrnd.png')
    #     bkgrnd = Image.new('RGBA', bkg.size)
    #     bkgrnd.paste(bkg)
    #     greyRect = Image.new('RGBA', bkg.size, (0,0,0,data.modeMenuBkgOpc))
    #     bkgrnd.paste(greyRect, box=(0,0), mask=greyRect)
    #     bkgrnd.save('temp.png', 'PNG')
    #     if data.belhaech<3:
    #         data.belhaech += 1
    #     elif data.belhaech==3:
    #         bkgrnd.show()
    #         data.belhaech=1000
    canvas.create_image(240, 160, image=PhotoImage(file='menuIcon.png'))
