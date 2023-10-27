from turtle import *
import random
number=[]
side=[forward,left,right]
color1=["yellow","blue","red","green","brown","black","purple","orange"]
for num in range(30,200):
    number.append(num)
for i in range(50):
    color(random.choice(color1))
    random.choice(side) (random.choice(number))
exitonclick()
