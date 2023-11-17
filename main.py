from tkinter import *
from turtle import ScrolledCanvas, RawTurtle, TurtleScreen
import random
from tkinter import Tk, Text
import tkinter as tk

root = Tk(className="Sumernosti")
canvas = ScrolledCanvas(root)
canvas=tk.Canvas(width=1000,height=1000) 
canvas.pack(side=LEFT)

screen = TurtleScreen(canvas)
turtle = RawTurtle(canvas)
turtle.hideturtle()



type=input("What type of")    

N=80
N=N/2





def type1():                                            #stredova sumernost
    stx=random.randint(30,200)
    sty=random.randint(30,200)
    
    canvas.create_oval(stx-N,sty-N,stx+N,sty+N)
    turtle.penup
    turtle.setposition(100, 100)
    turtle.pendown
    stxs=0
    stys=0
    turtle.pensize(5)
    turtle.fd(0)
    turtle.pensize(1)

def type2():                                            #osova sumernost
    stx=random.randint(30,200)
    sty=random.randint(30,200)
    canvas.create_oval(stx-N,sty-N,stx+N,sty+N)
    canvas.create_line(0,0,0,500)
    canvas.create_line(stx,sty,0,sty)
    
    
   
    
    

def type3():                                            #posunutie
    stx=random.randint(30,200)
    sty=random.randint(30,200)
    canvas.create_oval(stx-N,sty-N,stx+N,sty+N)




def type4():                                            #rotacia
    stx=random.randint(30,200)
    sty=random.randint(30,200)    
    canvas.create_oval(stx-N,sty-N,stx+N,sty+N)





if type == "1":
    type1()
if type == "2":
    type2()
if type == "3":
    type3()
if type == "4":
    type4()

root.mainloop()

