from tkinter import *
from time import time
from math import *
from random import *

a=Tk()
canvas=Canvas(a, width=400, height=300, bg='black')
canvas.pack()
canvas.focus_set()

state = False
kropki=[]


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
    def __init__(self, coords, friend=None, enemy=None):
        self.x=coords[0]
        self.y=coords[1]
        self.render()
        
    def __repr__(self):
        return '<Kropka nr>'
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def render(self):
        canvas.create_oval(self.x - 5, self.y - 5,self.x + 5,self.y + 5, fill='white')
        
    def follow(self, x=None):
        if x is None:
            x = self.friend
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
                for e in kropki:
                    e.run()
                    e.follow()
                    e.render()
        a.update_idletasks()
        a.update()
    except:
        break
