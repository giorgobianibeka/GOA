# რენდომად დახატული თართლი

from turtle import *
import random

speed(100)
colors=["red","green","blue","purple","yellow"]
for i in range(10000):
    width(random.randint(1,10))
    color(random.choice(colors))
    forward(random.randint(0,100))
    left(random.randint(0,100))
exitonclick