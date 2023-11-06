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

stxs=0
stys=0
turtle.pensize(5)
turtle.fd(0)
turtle.pensize(1)

type=input("What type of")    

N=int(input("Diameter of oval"))
N=N/2
def type1():                                            #stredova sumernost
    canvas.create_oval(stx-N,sty-N,stx+N,sty+N)
    turtle.setposition(100, -110)

if type=="1":
    type1()






screen.mainloop()

