from tkinter import *
from time import sleep
from random import randint
from turtle import heading


class Field:
    def __init__(self, c, n, m, width, height, walls=False):
        """
        c - canvas instance
        n - number of rows
        m - number of columns
        width - width of game field in pixels
        height - width of game field in pixels
        walls - if True matrix should have 0's surrounded by 1's (walls)
        example
        1 1 1 1
        1 0 0 1
        1 1 1 1
        """
        self.c = c
        self.a = []
        self.n = n
        self.m = m
        self.width = width
        self.height = height
        self.count = 0
        for i in range(n):
            self.a.append([])
            for j in range(m):
                if (i == 0) or (i == m - 1):
                    self.a[i].append(1)
                elif (j == 0) or (j == n - 1):
                    self.a[i].append(1)
                else:
                    if j == randint(1, (n - 1)) and self.count == 0:
                        self.a[i].append(2)
                        self.count += 1
                        continue
                    else:
                        self.a[i].append(0)

        self.draw(self.a)

    def print_field(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.a[i][j], end="")
            print()

    def draw(self, arr):
        """
        draw each element of matrix as a rectangle with white background and wall rectangle should have dark grey background
        """
        color = "grey"
        sizen = self.width // self.n
        sizem = self.height // self.m
        
        for i in range(self.n):
            drawed = False
            for j in range(self.m):
                if arr[i][j] == 1:
                    color = "grey"
                    self.draw_rect(
                        i * sizen,
                        j * sizem,
                        (i + 1) * sizen,
                        (j + 1) * sizem,
                        color=color,
                    )
                    continue
                elif arr[i][j] == 2:
                    color = "green"
                    if not drawed:
                        self.draw_rect(
                            j * sizem,
                            i * sizen,
                            (j + 1) * sizem,
                            (i + 1) * sizen,
                            color="black",
                        )
                        continue
                    drawed = True
                    continue
                else:
                    color = "white"
                    self.draw_rect(
                        i * sizen,
                        j * sizem,
                        (i + 1) * sizen,
                        (j + 1) * sizem,
                        color=color,
                    )

                # # if color == "green":
                # #     self.c.create_rectangle(j * sizem, i * sizen, (j + 1) * sizem, (i + 1) * sizen, fill="green")
                # # else:
                # self.c.create_rectangle(i * sizen, j * sizem, (i + 1) * sizen, (j + 1) * sizem, fill=color)

    def draw_rect(self, x1, y1, x2, y2, color):
        self.c.create_rectangle(x1, y1, x2, y2, fill=color)


class Player:
    def __init__(self, c, x, y, size, color="RED"):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.c = c
        self.body = self.c.create_oval(
            self.x - self.size / 2,
            self.y - self.size / 2,
            self.x + self.size / 2,
            self.y + self.size / 2,
            fill=self.color,
        )

    def moveto(self, x, y):
        self.mx = x
        self.my = y
        self.dx = (self.mx - self.x) / 50
        self.dy = (self.my - self.y) / 50
        self.draw()

    def draw(self):

        self.x += self.dx
        self.y += self.dy
        self.c.move(self.body, self.dx, self.dy)

        print(abs(self.x))
        if abs(self.mx - self.x) > 2:
            self.c.after(100, self.draw)

    def distance(self, x, y):
        return ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5


root = Tk()
root.geometry("400x400")
c = Canvas(root, width=800, height=800)
c.pack()

f = Field(c, 5, 5, 400, 400)
f.print_field()

"""
p1 = Player(c, 25, 25, 20, "GREEN")
p2 = Player(c, 375, 25, 20, "RED")
 
p1.moveto(150, 200)
p2.moveto(200, 300)
"""

root.mainloop()
# c.create_oval(p.x + 5,p.y + 5,p.x+p.size + 5,p.y+p.size + 5)
