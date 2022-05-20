import tkinter
import random

canvas = tkinter.Canvas(width=500, height=500, bg = "brown")
canvas.pack()
farba = "white"
for i in range(8):
    for j in range(8):
        canvas.create_rectangle(50 + j*50, 50 + i*50, 50 + j*50 + 50, 50 + i*50 + 50, fill = farba)
        if j != 7:
            if farba == "white":
                farba = "black"
            else:
                farba = "white"

white = []
black = []
r = 23
tile = 50
tah = "w"
turn = canvas.create_text(250, 475, text = "Na tahu", fill = "yellow", font = "arial 20")
for i in range(4):
    k = canvas.create_oval(75 + i*100 - r, 425 - r, 75 + i*100 + r, 425 + r, fill="white")
    white.append(k)
    k = canvas.create_oval(125 + i * 100 - r, 375 - r, 125 + i * 100 + r, 375 + r, fill="white")
    white.append(k)

for i in range(4):
    k = canvas.create_oval(75 + i*100 - r, 125 - r, 75 + i*100 + r, 125 + r, fill="black", outline = "white")
    black.append(k)
    k = canvas.create_oval(125 + i * 100 - r, 75 - r, 125 + i * 100 + r, 75 + r, fill="black", outline="white")
    black.append(k)

def klik(event):
    global kruh
    global tah
    global _x, _y
    if tah == "w":
        for i in white:
            koor = canvas.coords(i)
            if koor[0] < event.x < koor[2] and koor[1] < event.y < koor[3]:
                kruh = i
                _x = koor[0] + r
                _y = koor[1] + r
    else:
        for i in black:
            koor = canvas.coords(i)
            if koor[0] < event.x < koor[2] and koor[1] < event.y < koor[3]:
                kruh = i
                _x = koor[0] + r
                _y = koor[1] + r

def tahanie(event):
    kde = canvas.coords(kruh)
    if kde[0] < event.x < kde[2] and kde[1] < event.y < kde[3]:
        canvas.coords(kruh, event.x - r, event.y - r, event.x + r, event.y + r)

def release(event):
    global tah
    global kruh
    global _x, _y
    kde = canvas.coords(kruh)
    xx = (event.x // (tile)) * (tile) + (tile // 2)
    yy = (event.y // (tile)) * (tile) + (tile // 2)
    if kde[0] < event.x < kde[2] and kde[1] < event.y < kde[3]:
        canvas.coords(kruh, xx - r, yy - r, xx + r, yy + r)

        if 50 < xx < 450 and 50 < yy < 450 and _y != yy and _x != xx and abs(xx - _x) == abs(yy - _y):
            if tah == "w":
                for i in black:
                    c = canvas.coords(i)
                    x_dis = c[0] + r - _x
                    y_dis = c[1] + r - _y
                    if y_dis == 0:
                        y_dis = 1
                    if x_dis/y_dis == (xx - _x)/(yy - _y) and abs(x_dis) < abs(xx - _x) and abs(y_dis) < abs(yy - _y) and x_dis*(xx - _x) > 0 and y_dis*(yy - _y) > 0:
                        canvas.coords(i, 0, 0, 0, 0)
                tah = "b"
                canvas.coords(turn, 250, 25)
                if 50 < yy < 100:
                    canvas.itemconfig(kruh, outline="yellow", width = 2)
            else:
                for i in white:
                    c = canvas.coords(i)
                    x_dis = c[0] + r - _x
                    y_dis = c[1] + r - _y
                    if y_dis == 0:
                        y_dis = 1
                    if x_dis/y_dis == (xx - _x)/(yy - _y) and abs(x_dis) < abs(xx - _x) and abs(y_dis) < abs(yy - _y) and x_dis*(xx - _x) > 0 and y_dis*(yy - _y) > 0:
                        canvas.coords(i, 0, 0, 0, 0)
                tah = "w"
                canvas.coords(turn, 250, 475)
                if 400 < yy < 450:
                    canvas.itemconfig(kruh, outline="yellow", width = 2)
        else:
            canvas.coords(kruh, _x - r, _y - r, _x + r, _y + r)
        kruh = None

canvas.bind("<1>", klik)
canvas.bind("<B1-Motion>", tahanie)
canvas.bind("<B1-ButtonRelease>", release)
canvas.mainloop()