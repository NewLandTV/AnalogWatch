import tkinter
import math
from datetime import datetime

class Clock(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.x = 150
        self.y = 150
        self.geometry("300x300")
        self.hourLength = 30
        self.canvas = tkinter.Canvas(self, bg="white")
        self.canvas.pack(expand="yes", fill="both")

        hourStick = self.canvas.create_line(self.x, self.y, self.x + self.hourLength, self.y + self.hourLength, width=3, fill="red")
        minStick = self.canvas.create_line(self.x, self.y, self.x + self.hourLength, self.y + self.hourLength, width=3, fill="red")
        secStick = self.canvas.create_line(self.x, self.y, self.x + self.hourLength, self.y + self.hourLength, width=1, fill="blue")

        self.sticks = [hourStick, minStick, secStick]

        fsize = 13
        fcolor = "black"

        self.canvas.create_text(10, 150, text="9", font=("나눔고딕코딩", fsize), fill=fcolor)
        self.canvas.create_text(150, 10, text="12", font=("나눔고딕코딩", fsize), fill=fcolor)
        self.canvas.create_text(290, 150, text="3", font=("나눔고딕코딩", fsize), fill=fcolor)
        self.canvas.create_text(150, 290, text="6", font=("나눔고딕코딩", fsize), fill=fcolor)

        w = 150
        h = 150
        r = 130
        x0 = w - r
        y0 = h - r
        x1 = w + r
        y1 = h + r

        self.canvas.create_oval(x0, y0, x1, y1)

    def UpdateClock(self):
        currentTime = datetime.now()
        strTime = currentTime.strftime("%I%M%S")

        _h = int(strTime[0:2]) * 5
        _m = int(strTime[2:4])
        _s = int(strTime[4:6])

        x, y = self.canvas.coords(self.sticks[0])[0:2]
        x2 = (self.hourLength + 50) * math.cos(math.radians(_h * 6) - math.radians(90)) + self.x
        y2 = (self.hourLength + 50) * math.sin(math.radians(_h * 6) - math.radians(90)) + self.y

        self.canvas.coords(self.sticks[0], tuple([x, y, x2, y2]))

        x, y = self.canvas.coords(self.sticks[1])[0:2]
        x2 = (self.hourLength + 90) * math.cos(math.radians(_m * 6) - math.radians(90)) + self.x
        y2 = (self.hourLength + 90) * math.sin(math.radians(_m * 6) - math.radians(90)) + self.y

        self.canvas.coords(self.sticks[1], tuple([x, y, x2, y2]))

        x, y = self.canvas.coords(self.sticks[2])[0:2]
        x2 = (self.hourLength + 90) * math.cos(math.radians(_s * 6) - math.radians(90)) + self.x
        y2 = (self.hourLength + 90) * math.sin(math.radians(_s * 6) - math.radians(90)) + self.y

        self.canvas.coords(self.sticks[2], tuple([x, y, x2, y2]))

if __name__ == "__main__":
    clock = Clock()
    
    while True:
        clock.update()
        clock.UpdateClock()