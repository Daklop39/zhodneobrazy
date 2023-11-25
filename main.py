import turtle
from turtle import RawTurtle, TurtleScreen
import tkinter as tk
from tkinter import *
import random

window = tk.Tk()
window.minsize(width = 720, height = 800)
canvas = Canvas(window, width = 720, height = 800,bd=0)
canvas.pack()

screen = TurtleScreen(canvas)
screen.setworldcoordinates(0, 800, 720, 0)

#screen.setworldcoordinates(-180, -90, 180, 90)
#canvas.create_line(0,0,720,800,fill="red")
#canvas.create_line(720,0,0,800,fill="red")
quake = RawTurtle(screen)
#quake.shape("circle")
#quake.color("red")
#quake.fd(0)
#quake.goto(720,800)

type=input("What type of")    

def type1():                                            #stredova sumernost
    N=50
    S=3
    stx=random.randint(30,200)
    sty=random.randint(30,200)
    stxS=random.randint(100,300)
    styS=random.randint(100,300)
    canvas.create_text(stxS+4,styS-10,text="Stred")
    canvas.create_oval(stxS,styS,stxS+S,styS+S,fill="black")
    canvas.create_oval(stx-N,sty-N,stx+N,sty+N)
    
   
    
    

def type2():                                            #osova sumernost
    N=80
    N=N/2
    stx=random.randint(30,200)
    sty=random.randint(30,200)
    canvas.create_text(50,-100,text=("Os sumernosti"))
    canvas.create_text(stx,sty-N-10,text="Vzor")
    canvas.create_oval(stx-N,sty-N,stx+N,sty+N)
    canvas.create_line(0,0,0,1100)
    canvas.create_line(stx,sty,stx-(2*stx),sty)
    canvas.create_text((stx-2*stx),sty-N-10,text="Obraz")
    canvas.create_oval((stx-2*stx)-N,sty-N,(stx-2*stx)+N,sty+N)
    
   
    
    

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

mainloop()

