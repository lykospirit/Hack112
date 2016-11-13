from tkinter import *
from PIL import Image

class Button(object):
    font = "Helvetica 24 bold"

    def __init__(self, l, t, r, b, name="", parent=""):
        self.name = name
        self.parent = parent
        self.l = l
        self.t = t
        self.r = r
        self.b = b
        self.cx = (r+l)//2
        self.cy = (t+b)//2

    def isPressed(self, x, y):
        if (self.l < x and x < self.r):
            if (self.t < y and y < self.b):
                return True
        return False

    def drawButton(self, canvas):
        canvas.create_rectangle(self.l, self.t, self.r, self.b, fill="cyan")
        if self.name:
            canvas.create_text(self.cx, self.cy, text=self.name, font=Button.font)

class CircleButton(Button):
    def __init__(self, l, t, r, b, name="", parent=""):
        super().__init__(l, t, r, b, name, parent)
        self.radius = (r-l)//2

    def isPressed(self, x, y):
        dist = ((self.cx - x)**2 + (self.cy - y)**2)**0.5
        if dist <= self.radius:
            return True
        return False

    def drawButton(self, canvas):
        canvas.create_oval(self.l, self.t, self.r, self.b, fill="cyan")
        if self.name:
            canvas.create_text(self.cx, self.cy, text=self.name, font=Button.font)

class ImageButton(Button):
    def __init__(self, l, t, name="", parent="", img=""):
        self.img = PhotoImage(file=img)
        self.imgWidth = Image.open(img).size[0]
        self.imgHeight = Image.open(img).size[1]
        super().__init__(l, t, l+self.imgWidth, t+self.imgHeight, name, parent)

    def drawButton(self, canvas):
        canvas.create_image(self.l, self.t, anchor=NW, image=self.img)
        if self.name:
            canvas.create_text(self.l+self.imgWidth/2, self.t+self.imgHeight/2,
                                                text=self.name, font=Button.font)
