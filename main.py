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



#type=input("What type of")    


def type1():                                            #stredova sumernost
    N=80
    quake.ht()
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
    quake.ht()
    
    N=80
    N=N/2
    stx=random.randint(100,800)
    sty=random.randint(100,800)
    canvas.create_line(500,0,500,1000)
    canvas.create_text(50,-100,text=("Os sumernosti"))
    
    if stx >= 500:
        quake.penup()
        mvx=stx-500
        canvas.create_text(stx,sty-N-10,text="Vzor")
        canvas.create_oval(stx-N,sty-N,stx+N,sty+N)
        quake.setposition(stx,sty)
        quake.pendown()
        quake.setposition(500-mvx,sty,)
        canvas.create_oval(500-mvx-N,sty-N,500-mvx+N,sty+N)
        canvas.create_text(500-mvx,sty-N-10,text="Obraz")
        quake.penup()
    
    if stx <= 500:
        quake.penup()
        mvx=500-stx
        canvas.create_text(stx,sty-N-10,text="Vzor")
        canvas.create_oval(stx-N,sty-N,stx+N,sty+N)
        quake.setposition(stx,sty)
        quake.pendown()
        quake.setposition(500+mvx,sty)
        canvas.create_oval(500+mvx-N,sty-N,500+mvx+N,sty+N)
        canvas.create_text(500+mvx,sty-N-10,text="Obraz")
        quake.penup()
    
    

def type3():                                            #posunutie
    stx=random.randint(30,200)
    
    




def type4():                                            #rotacia
    stx=random.randint(30,200)
    




button= Button(window,text= "stredová súmernosť", command=lambda : type1())
button.place(relx=0,x=850,y=70,anchor = W)

button= Button(window,text= "osová súmernosť", command=lambda : type2())
button.place(relx=0,x=855,y=100,anchor = W)

button= Button(window,text= "posunutie", command=lambda : type3())
button.place(relx=0,x=875,y=130,anchor = W)

button= Button(window,text= "rotácia", command=lambda : type4())
button.place(relx=0,x=883,y=160,anchor = W)

mainloop()

