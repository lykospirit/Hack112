#####
# Main Menu
#####

from Button import *

def initMainMenu(data):
    data.mainMenuBkgOpc = 0
    data.greyBk = ImageButton(0, 0, img="temp.png")
    data.profilePic = "kosbieProfile.png"
    data.profileName = "112 God"
    data.workoutButton = Button(0, 40, 160, 80, name="workout", color="#92d4be", parent="MainMenu")
    data.profileButton = Button(0, 80, 160, 120, name="profile", color="#87cdb6", parent="MainMenu")
    data.historyButton = Button(0, 120, 160, 160, name="history", color="#92d4be", parent="MainMenu")

    data.activeButtons = []
    data.activeButtons.append(data.greyBk)
    data.activeButtons.append(data.workoutButton)

def mainMenuMousePressed(event, data, button):
    data.mainMenuActive = False

def mainMenuTimerFired(data):
    pass

def mainMenuRedrawAll(canvas, data):
    if (data.mainMenuActive and data.mainMenuBkgOpc<120) or (not data.mainMenuActive and data.mainMenuBkgOpc>0):
        if data.mainMenuActive and data.mainMenuBkgOpc<120:
            data.mainMenuBkgOpc += 40
        else: data.mainMenuBkgOpc -= 40
        bkg = Image.open('mainBkgrnd.png')
        bkgrnd = Image.new('RGBA', bkg.size)
        bkgrnd.paste(bkg)
        greyRect = Image.new('RGBA', bkg.size, (0,0,0,data.mainMenuBkgOpc))
        bkgrnd.paste(greyRect, box=(0,0), mask=greyRect)
        bkgrnd.save('temp.png', 'PNG')
    data.greyBk = ImageButton(0, 0, img="temp.png")
    data.greyBk.drawButton(canvas)
    if data.mainMenuBkgOpc >= 120:
        canvas.create_rectangle(0, 0, 160, 280, fill="#78c0a8", width=0)
        canvas.create_rectangle(0, 0, 160, 40, fill="#354458", width=0)
        kosbie = ImageCircleButton(10, 5, img=data.profilePic)
        kosbie.drawButton(canvas)
        canvas.create_text(50, 20, anchor="w", text=data.profileName, font="Helvetica 10 bold", fill="white")
        data.workoutButton.drawButton(canvas)
        data.profileButton.drawButton(canvas)
        data.historyButton.drawButton(canvas)
        canvas.create_text(25, 60, anchor="w", text="Workout", font="Helvetica 10 bold", fill="black")
        canvas.create_text(25, 100, anchor="w", text="Profile", font="Helvetica 10 bold", fill="black")
        canvas.create_text(25, 140, anchor="w", text="History", font="Helvetica 10 bold", fill="black")
