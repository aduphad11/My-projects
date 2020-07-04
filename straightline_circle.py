#fake circle using Straight lines

from turtle import*
from math import sin,cos,pi
r=200
inc=2*pi/100
t=0;n=1.5
for i in range(100):
    x1=r*sin(t);y1=r*cos(t)
    x2=r*sin(t+n);y2=r*cos(t+n)
    penup();goto(x1,y1)
    pendown();goto(x2,y2)
    t=t+inc

