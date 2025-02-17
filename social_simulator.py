from tkinter import *
from time import time
from math import *
from random import *
a=Tk()
canvas=Canvas(a, bg='black')
canvas.pack()
kropki=[]
canvas.focus_set()
state = False

def take_coords(ev):
    global kropki
    kropki += [Kropka([ev.x, ev.y])]
    for e in kropki:
        e.f = choice(kropki[:-1]) if len(kropki)>1 else None
        e.enemy = choice(kropki[:-1]) if len(kropki)>1 else None

def switch(ev):
    global state
    state = not state
        
canvas.bind('<Button-1>', take_coords)
canvas.bind('<space>', switch)
    

class Kropka:
    def __init__(self, coords, f=None, enemy=None):
        self.x=coords[0]
        self.y=coords[1]
        self.render()
    def __repr__(self):
        return '<Kropka x='+str(self.x)+' y='+str(self.y)+'>'
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def render(self):
        canvas.create_oval(self.x - 5, self.y - 5,self.x + 5,self.y + 5, fill='white')
    def follow(self, x=None):
        if x is None:
            x = self.f
        if x:
            dx=(x.x-self.x)/100
            dy=(x.y-self.y)/100
            self.move(dx, dy)
    def run(self, x=None):
        if x is None:
            x=self.enemy
        if x and x.x != self.x and x.y != self.y:
            dx=5/-(x.x-self.x)
            dy=5/-(x.y-self.y)
            self.move(dx, dy)
            
        
        
b=time()
while 1:
    try:
        if state:
            if time() > b+.005:
                b = time()
                canvas.delete('all')
                total = 0
                for e in kropki:
                    e.run()
                    e.follow()
                    e.render()
                    total = total + 1
                    canvas.create_oval(1, 1, 1, 1, fill='white')
        a.update_idletasks()
        a.update()
    except:
        break

