from tkinter import *
from time import time
from math import *
from random import *

a=Tk()
canvas=Canvas(a, width=500, height=400, bg='black')
canvas.pack()
canvas.focus_set()

state = False
kropki=[]
b=time()

def take_coords(ev):
    global kropki
    kropki += [Kropka([ev.x, ev.y])]
    for e in kropki:
        e.friend = choice(kropki) if len(kropki)>1 else None
        while e == e.friend:
            e.friend = choice(kropki)
        e.enemy = choice(kropki) if len(kropki)>2 else None
        while (e == e.enemy or e.friend == e.enemy) and e.friend != None:
            e.enemy = choice(kropki)

            
           # if e == e.friend.enemy

def switch(ev):
    global state
    state = not state

def debug(ev):
    for e in kropki:
        print('<kropka nr '+str(kropki.index(e))+' przyjaciel:',end=' ')
        if e.friend in kropki:
            print(str(kropki.index(e.friend)),end=' ')
        else:
            print('None',end = ' ')
        print(', wróg: ',end = ' ')
        if e.enemy in kropki:
            print(str(kropki.index(e.enemy)))
        else:
            print('None')
    print('')

def getcolor():
    return ("#"+''.join([choice('0123456789ABCDEF') for j in range(6)]))

"""def clear(ev):
    for e in kropki:
        kropki.remove(e)"""
        
    
  
canvas.bind('<Button-1>', take_coords)
canvas.bind('<space>', switch)
canvas.bind('<r>', debug)
#canvas.bind('<c>', clear)

class Kropka:
    def __init__(self, coords, friend=None, enemy=None):
        self.x=coords[0]
        self.y=coords[1]
        self.render()
        self.friend=friend
        self.enemy=enemy
        self.color=getcolor()
        
    def __repr__(self):
        return str(kropki.index(self))
    
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
            

while 1:
    try:
        if state:
            if time() > b+.001:
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

