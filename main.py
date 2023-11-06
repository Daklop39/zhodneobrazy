from tkinter import *
from turtle import ScrolledCanvas, RawTurtle, TurtleScreen
import random
from tkinter import Tk, Text
root = Tk()
canvas = ScrolledCanvas(root)
canvas.pack(side=LEFT)

screen = TurtleScreen(canvas)
turtle = RawTurtle(canvas)
turtle.hideturtle()
stx=random.randint(10,100)
sty=random.randint(10,100)



type=input("What type of")    

N=int(input("Diameter of oval"))
N=N/2
def type1():                                            #stredova sumernost
    canvas.create_oval(stx-N,sty-N,stx+N,sty+N)
    turtle.penup
    turtle.setposition(stx, sty)
    turtle.pendown
    stxs=0
    stys=0
    turtle.pensize(5)
    turtle.fd(0)
    turtle.pensize(1)

def type2():                                            #osova sumernost
    canvas.create_oval(stx-N,sty-N,stx+N,sty+N)
    canvas.create_line(0,0,0,100)

def type3():                                            #posunutie
    canvas.create_oval(stx-N,sty-N,stx+N,sty+N)




def type4():                                            #rotacia
    canvas.create_oval(stx-N,sty-N,stx+N,sty+N)





if type == "1":
    type1()

if type == "2":
    type2()
if type == "3":
    type3()
if type == "4":
    type4()

screen.mainloop()

