import tkinter

canvas = tkinter.Canvas(width = 500, height = 600)
canvas.pack()
r = 15
outer = []
middle = []
inner = []
colors = ["red", "white"]
player = 0
white = 0
red = 0
white_counter = canvas.create_text(250, 40, text = "White: 0", font = "Arial 20")
red_counter = canvas.create_text(250, 80, text = "Red: 0", font = "Arial 20")
indicator = canvas.create_oval(235 - 75, 65, 265 - 75, 95, fill = "red", width = 3)
for i in range(3):
    o = []
    m = []
    ii = []
    if i == 1:
        for j in range(2):
            k = canvas.create_oval(0 - r, 0 - r, 0 + r, 0 + r, fill = "black")
            o.append(k)
            k = canvas.create_oval(0 - r, 0 - r, 0 + r, 0 + r, fill = "black")
            m.append(k)
            k = canvas.create_oval(0 - r, 0 - r, 0 + r, 0 + r, fill = "black")
            ii.append(k)
    else:
        for j in range(3):
            k = canvas.create_oval(0 - r, 0 - r, 0 + r, 0 + r, fill = "black")
            o.append(k)
            k = canvas.create_oval(0 - r, 0 - r, 0 + r, 0 + r, fill = "black")
            m.append(k)
            k = canvas.create_oval(0 - r, 0 - r, 0 + r, 0 + r, fill = "black")
            ii.append(k)
    outer.append(o)
    middle.append(m)
    inner.append(ii)

board = [outer, middle, inner]
s = [250, 350]
rr = 200
for i, ring in enumerate(board):
    for j, row in enumerate(ring):
        for k, item in enumerate(row):
            if j == 1:
                cr = 200 - i*60
                canvas.coords(item, s[0] + ((-0.5 + k)*2)*cr - r, s[1] + (-1 + j)*cr - r, s[0] + ((-0.5 + k)*2)*cr + r, s[1] + (-1 + j)*cr + r)
            else:
                cr = 200 - i*60
                canvas.coords(item, s[0] + (-1 + k)*cr - r, s[1] + (-1 + j)*cr - r, s[0] + (-1 + k)*cr + r, s[1] + (-1 + j)*cr + r)

for i in range(2):
    l = canvas.create_line(s[0], s[1] + 80*((-0.5 + i)*2), s[0], s[1] + 200*((-0.5 + i)*2), width = 5)
    ll = canvas.create_line(s[0] + 80*((-0.5 + i)*2), s[1], s[0] + 200*((-0.5 + i)*2), s[1], width = 5)
    canvas.tag_lower(l)
    canvas.tag_lower(ll)

for i in range(3):
    l = canvas.create_rectangle(s[0] - (200 - i*60), s[1] - (200 - i*60), s[0] + (200 - i*60), s[1] + (200 - i*60), width = 5)
    canvas.tag_lower(l)

def klik(e):
    global board, player, point_count
    for ring in board:
        for row in ring:
            for item in row:
                coor = canvas.coords(item)
                if coor[0] <= e.x <= coor[2] and coor[1] <= e.y <= coor[3]:
                    canvas.itemconfig(item, fill = colors[player % 2], width = 3)
                    player += 1
    point_count()

def point_count():
    global board, white, red
    white = 0
    red = 0
    for i, ring in enumerate(board):
        for j, row in enumerate(ring):
            colors_in_row = []
            taken_in_row = 0
            for k, item in enumerate(row):
                conf = canvas.itemconfig(item)
                if conf["fill"][-1] not in colors_in_row and int(conf["width"][-1][0]) > 2:
                    colors_in_row.append(conf["fill"][-1])
                if int(conf["width"][-1][0]) > 2:
                    taken_in_row += 1
                if j == 0 and int(conf["width"][-1][0]) > 2 and k != 1:
                    if k == 2:
                        conf1 = canvas.itemconfig(ring[1][k - 1])
                    else:
                        conf1 = canvas.itemconfig(ring[1][k])
                    conf2 = canvas.itemconfig(ring[2][k])
                    k = 2
                    if conf["fill"][-1] == conf1["fill"][-1] and conf["fill"][-1] == conf2["fill"][-1]:
                        if conf["fill"][-1] == "white":
                            white += 1
                        else:
                            red += 1
                if i == 2:
                    if j != 1 and k == 1 and int(conf["width"][-1][0]) > 2:
                        conf1 = canvas.itemconfig(board[1][j][k])
                        conf2 = canvas.itemconfig(board[0][j][k])
                        if conf["fill"][-1] == conf1["fill"][-1] and conf["fill"][-1] == conf2["fill"][-1]:
                            if conf["fill"][-1] == "white":
                                white += 1
                            else:
                                red += 1
                    elif j == 1 and int(conf["width"][-1][0]) > 2:
                        conf1 = canvas.itemconfig(board[1][j][k])
                        conf2 = canvas.itemconfig(board[0][j][k])
                        if conf["fill"][-1] == conf1["fill"][-1] and conf["fill"][-1] == conf2["fill"][-1]:
                            if conf["fill"][-1] == "white":
                                white += 1
                            else:
                                red += 1
            if len(colors_in_row) == 1 and taken_in_row == 3:
                if colors_in_row[0] == "white":
                    white += 1
                else:
                    red +=1
                
    canvas.itemconfig(white_counter, text = f"White: {white}")
    canvas.itemconfig(red_counter, text = f"Red: {red}")
    indconf = canvas.itemconfig(indicator)
    indcoor = canvas.coords(indicator)
    if indconf["fill"][-1] == "red":
        canvas.coords(indicator, indcoor[0], indcoor[1] - 40, indcoor[2], indcoor[3] - 40)
        canvas.itemconfig(indicator, fill = "white")
    else:
        canvas.coords(indicator, indcoor[0], indcoor[1] + 40, indcoor[2], indcoor[3] + 40)
        canvas.itemconfig(indicator, fill = "red")

canvas.bind("<1>", klik)
canvas.mainloop()