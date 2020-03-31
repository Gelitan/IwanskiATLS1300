# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 09:28:55 2020

@author: mwnew
"""

#========
#PC06-Revise and Critique
#Analise Iwanski
#200305
#
#This is the code created by Mickie Newman for her PC03 Generative Art lab
#========

from turtle import *
from random import *

colors = ['#D7263D','#F46036','#2E294E','#1B998B','#C5D86D'] #defining the random colors
square = Turtle()    

#putting square like things in random places
for i in range(1000):
    square.color(colors[randint(0,4)])
    square.width(5)
    square.up()
    square.right(randint(0,360))
    square.forward(randint(0,300))
    square.down()
    for i in range(4): #drawing the shapes
        square.forward(randint(50,100))
        square.right(90)

done()