from turtle import Turtle

def triangle(u,s):
    for i in range(3):
            t.forward(u)
            t.lt(120)
    t.rt(60)
    t.forward(s)

def hexagon(u,s):
    i=0
    while(i<=5):
        triangle(50,50)
        i+=1

t=Turtle()
size=100
hexagon(t,size)
#2-3
    
        
        
