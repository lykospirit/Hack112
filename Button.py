from tkinter import *
from PIL import Image

class Button(object):
    font = "Helvetica 24 bold"

    def __init__(self, l, t, r, b, name="", parent="", color=""):
        self.name = name
        self.parent = parent
        self.color = color
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
        canvas.create_rectangle(self.l, self.t, self.r, self.b, fill=self.color, width=0)

class CircleButton(Button):
    def __init__(self, l, t, r, b, name="", parent="", color=""):
        super().__init__(l, t, r, b, name, parent, color)
        self.radius = (r-l)//2

    def isPressed(self, x, y):
        dist = ((self.cx - x)**2 + (self.cy - y)**2)**0.5
        if dist <= self.radius:
            return True
        return False

    def drawButton(self, canvas):
        canvas.create_oval(self.l, self.t, self.r, self.b, fill=self.color, width=0)

class ImageButton(Button):
    def __init__(self, l, t, img, name="", parent=""):
        self.img = PhotoImage(file=img)
        im = Image.open(img)
        self.imgWidth, self.imgHeight = im.size
        super().__init__(l, t, l+self.imgWidth, t+self.imgHeight, name, parent)

    def drawButton(self, canvas):
        canvas.create_image(self.l, self.t, anchor=NW, image=self.img)

class ImageCircleButton(ImageButton):
    def __init__(self, l, t, img, name="", parent=""):
        super().__init__(l, t, img, name, parent)
        self.cx, self.cy = l+self.imgWidth//2, t+self.imgHeight//2
        self.radius = self.imgWidth//2

    def isPressed(self, x, y):
        dist = ((self.cx - x)**2 + (self.cy - y)**2)**0.5
        if dist <= self.radius:
            return True
        return False

    def drawButton(self, canvas):
        canvas.create_image(self.cx, self.cy, image=self.img)
