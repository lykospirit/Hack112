class Button(object):
    def __init__(self, l, t, r, b, name="", parent=""):
        self.name = name
        self.parent = parent
        self.l= l
        self.t = t
        self.r = r
        self.b = b

    def isPressed(self, x, y):
        if (self.l < x and x < self.r):
            if (self.t < y and y < self.b):
                return True
        return False

    def drawButton(self, canvas):
        l = self.l
        t = self.t
        r = self.r
        b = self.b
        canvas.create_rectangle(l, t, r, b, fill="cyan")
        if self.name:
            canvas.create_text((l+r)/2, (t+b)/2, text=self.name,
                                font="Helvetica 24 bold")

class CircleButton(object):
    
