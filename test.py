walk=[]
while True:
    v=input("R,L,F,0を入れてね")
    if v!=0:
        walk.append(v)
    elif v==0:
        break
print(walk)

from turtle import Turtle
t=Trutle()

F=(t.forward(100))
R=(t.rt(90))
L=(t.lt(90))

n=len(walk)
while True:
    k=0
    if k<=n:
        walk[k]
        k=k+1
    elif k>n:
        break



