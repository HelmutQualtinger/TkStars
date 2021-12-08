import numpy as np
from tkinter import *
import random

def rgb_hack(rgb):
    return "#%02x%02x%02x" % (rgb[0],rgb[1],rgb[2])

StarNum=1
def DrawStar(w, pos, divisions, size, color):
    global StarNum
    x = np.arange(0, size, size / divisions, dtype=int)
    y = np.flip(x)
    px, py = pos
    #   w.create_line(0, y, canvas_width, y, fill="#476042")
    for i in range(divisions):
        w.create_line(x[i] + px, py,
                      px, y[i] + py,
                      px - x[i], py,
#                      px, y[i] + py,
                      px, py - y[i],
                      x[i] + px, py,
                      fill=color,width=1,tag="Star"+str(StarNum))
  #      w.create_line(, px, py - y[i], fill=color,width=3,tag="Star"+str(StarNum))
  #      w.create_line(px - x[i], py,, fill=color,width=4,tag="Star"+str(StarNum))
    StarNum+=1
    return

def BackGround():
#    print("Backgound")
    global StarNum
    for star in range(StarNum):
        x=int(random.randint(-3,3))
        y=int(random.randint(-3,3))
        w.move("Star"+str(star),x,y)
    master.after(10,BackGround)


master = Tk()
canvas_width = 2096
canvas_height = 1200

w = Canvas(master, width=canvas_width, height=canvas_height, bg="black")
w.pack()
uc=0
w.create_rectangle(0,0,canvas_width,canvas_height,fill="#000020")
for stars in range(random.randint(200, 600)):
    xp = random.randint(0, canvas_width)
    yp = random.randint(0, canvas_height)
    steps = random.randint(15, 25)
    size = random.randint(5, 50)
    color = [random.randint(0, 255) for i in range(3)]
    rgb = rgb_hack(color)
    DrawStar(w, (xp, yp), steps, size, rgb)
    if uc%10==0: master.update()
    uc+=1
master.after(10,BackGround)
w.postscript(file="Stars.ps")
mainloop()
