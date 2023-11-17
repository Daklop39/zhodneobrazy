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

def quit():
    root.destroy()

if type !="1234":
    quit()






def type1():                                            #stredova sumernost
    N=3
    stx=random.randint(30,200)
    sty=random.randint(30,200)
    stxS=random.randint(-100,100)
    styS=(-100,100)
    canvas.create_oval(stxS,styS,stxS+N,styS+N,fill="black")
    canvas.create_oval(stx-N,sty-N,stx+N,sty+N)
    
   
    
    

def type2():                                            #osova sumernost
    N=80
    N=N/2
    stx=random.randint(30,200)
    sty=random.randint(30,200)
    canvas.create_text(50,-100,text=("Os sumernosti"))
    canvas.create_oval(stx-N,sty-N,stx+N,sty+N)
    canvas.create_line(0,-1000,0,1000)
    canvas.create_line(stx,sty,stx-(2*stx),sty)
    
    
   
    
    

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

