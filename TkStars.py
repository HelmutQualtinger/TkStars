import numpy as np
from tkinter import *
import random

def rgb_hack(rgb):
    """
    translate rgb tuple into a colorstring for tk
    :cvar
    """
    return "#%02x%02x%02x" % (rgb[0],rgb[1],rgb[2])

StarNum=1
def DrawStar(w, pos, divisions, size, color):
    """
    Draw a single stars with following parameters. Stars are tagged so they van later by moved by tag
    :param w:   canvas to be drawn in
    :param pos:  where to initially appear ntuple x and y in canvas coordinates
    :param divisions:  grid divisions of star
    :param size:       radius of star
    :param color:      TK color of star
    :return:
    """
    global StarNum
    x = np.arange(0, size, size / divisions, dtype=int)
    y = np.flip(x)
    px, py = pos
    #   w.create_line(0, y, canvas_width, y, fill="#476042")
    for i in range(divisions):
        w.create_line(x[i] + px, py,
                      px, y[i] + py,
                      px - x[i], py,
                      px, py - y[i],
                      x[i] + px, py,
                      fill=color,width=1,tag="Star"+str(StarNum))

    StarNum+=1
    return

def BackGround():
    """
    Runs in Background slightly moves the stars and reschedules it self
    """
    print("Backgound")
    global StarID
    for star in range(StarNum):
        pass
        if random.random()<0.01:
            x = int(random.randint(-10, 10))
            y = int(random.randint(-8, 8))
            w.move("Star"+str(star), x, y)
            color = [random.randint(0, 255) for i in range(3)]
            rgb = rgb_hack(color)  # translate colors into something tk under stands
            w.itemconfig("Star"+str(star),fill=rgb)

        if random.random()<0.02:
            color = [random.randint(0, 255) for i in range(3)]
            rgb = rgb_hack(color)  # translate colors into something tk under stands
            w.itemconfig("Star"+str(star),fill="black")

        x = int(random.randint(-1, 1))
        y = int(random.randint(-1, 1))
        w.move("Star"+str(star), x, y)
    master.after(10, BackGround)


master = Tk()  # init tk
canvas_width = 2096     # define canvas size
canvas_height = 1200

w = Canvas(master, width=canvas_width, height=canvas_height, bg="black")
w.pack()  # create and place canvas
uc=0
w.create_rectangle(0,0,canvas_width,canvas_height,fill="#000020") # draw very darkblue sky to also appear on print
for stars in range(random.randint(800, 1600)):  # create random number of stars
    xp = random.randint(0, canvas_width)       # with random attributes
    yp = random.randint(0, canvas_height)
    steps = random.randint(4, 10)
    size = random.randint(5, 50)
    color = [random.randint(0, 255) for i in range(3)]
    rgb = rgb_hack(color)    # translate colors into something tk under stands
    DrawStar(w, (xp, yp), steps, size, rgb)
    if uc%1==0: master.update()   # let the stars appear gradually
    uc+=1
master.after(10,BackGround)      # schedule Braunian movement of stars
w.postscript(file="Stars.ps")    # print a file as a souvenir
mainloop()                       # tk mainloop
