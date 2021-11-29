import numpy as np
from tkinter import *
import random

def rgb_hack(rgb):
    return "#%02x%02x%02x" % (rgb[0],rgb[1],rgb[2])

def DrawStar(w, pos, divisions, size, color):
    x = np.arange(0, size, size / divisions, dtype=int)
    y = np.flip(x)
    px, py = pos
    #   w.create_line(0, y, canvas_width, y, fill="#476042")
    for i in range(divisions):
        w.create_line(x[i] + px, py, px, y[i] + py, fill=color,width=1)
        w.create_line(px - x[i], py, px, y[i] + py, fill=color,width=2)
        w.create_line(x[i] + px, py, px, py - y[i], fill=color,width=3)
        w.create_line(px - x[i], py, px, py - y[i], fill=color,width=4)
    return
master = Tk()
canvas_width = 2000
canvas_height = 800
w = Canvas(master, width=canvas_width, height=canvas_height, bg="black")
w.pack()
uc=0
for stars in range(random.randint(100, 300)):
    xp = random.randint(0, canvas_width)
    yp = random.randint(0, canvas_height)
    steps = random.randint(5, 8)
    size = random.randint(5, 70)
    color = [random.randint(0, 255) for i in range(3)]
    rgb = rgb_hack(color)
    DrawStar(w, (xp, yp), steps, size, rgb)
    if uc%1==0: master.update()
    uc+=1

mainloop()