import turtle
from turtle import RawTurtle, TurtleScreen
import tkinter as tk
from tkinter import *
import random

window = tk.Tk()
window.minsize(width = 1000, height = 1000)
canvas = Canvas(window, width = 1000, height = 1000,bd=0)
canvas.pack()
screen = TurtleScreen(canvas)
screen.setworldcoordinates(0, 1000, 1000, 0)
quake = RawTurtle(screen)

type=input("What type of")    

quake.ht()
def type1():                                            #stredova sumernost
    N=80
    
    stx=random.randint(100,900)
    sty=random.randint(110,900)
    stxS=500
    styS=500
    canvas.create_text(stxS+4,styS-10,text="Stred")
    canvas.create_text(stx+7,sty,text="S")
    canvas.create_oval(stx-2,sty-2,stx+2,sty+2,fill="black")
    canvas.create_oval(stxS-2,styS-2,stxS+2,styS+2,fill="black")
    canvas.create_oval(stx-N,sty-N,stx+N,sty+N)
    
    quake.penup()
    quake.setposition(stx,sty)
    quake.pendown()
    quake.setposition(stxS,styS)
   
    if stxS>= stx and styS>= sty:    #2.kv
        mvx= stxS-stx
        mvy= styS-sty
        quake.setposition(stxS+mvx,styS+mvy)
        canvas.create_oval(stxS+mvx-N,styS+mvy-N,stxS+mvx+N,styS+mvy+N)
        canvas.create_oval(stxS+mvx-2,styS+mvy-2,stxS+mvx+2,styS+mvy+2,fill="black")
        canvas.create_text(stxS+mvx,styS+mvy+10,text="S'")
    
    if stxS>= stx and styS<= sty:    #3.kv
        mvx= stxS-stx
        mvy= sty-styS
        quake.setposition(stxS+mvx,styS-mvy)
        canvas.create_oval(stxS+mvx-N,styS-mvy-N,stxS+mvx+N,styS-mvy+N)
        canvas.create_oval(stxS+mvx-2,styS-mvy-2,stxS+mvx+2,styS-mvy+2,fill="black")
        canvas.create_text(stxS+mvx+7,styS-mvy,text="S'")
    
    if stxS<= stx and styS<= sty:    #4.kv
        mvx= stx-stxS
        mvy= sty-styS
        quake.setposition(stxS-mvx,styS-mvy)
        canvas.create_oval(stxS-mvx-N,styS-mvy-N,stxS-mvx+N,styS-mvy+N)
        canvas.create_oval(stxS-mvx-2,styS-mvy-2,stxS-mvx+2,styS-mvy+2,fill="black")
        canvas.create_text(stxS-mvx-7,styS-mvy,text="S'")
    
    if stxS<= stx and styS>= sty:    #1.kv   
        mvx= stx-stxS
        mvy= styS-sty   
        quake.setposition(stxS-mvx,styS+mvy)
        canvas.create_oval(stxS-mvx-N,styS+mvy-N,stxS-mvx+N,styS+mvy+N)
        canvas.create_oval(stxS-mvx-2,styS+mvy-2,stxS-mvx+2,styS+mvy+2,fill="black")
        canvas.create_text(stxS-mvx,styS+mvy+10,text="S'")



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

