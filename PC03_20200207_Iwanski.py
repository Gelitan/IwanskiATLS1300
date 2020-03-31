#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 09:50:03 2020

@author: analiseiwanski
"""
#========
#PC03-Generative Art
#Analise Iwanski
#200207
#
#This code creates art based on random numbers dictating the angles, start and end positions, and colors. I was inspired by DNA depictions (see inspiration in submission)
#I used nested loops and random integers and random choices to make a new set of colorful lines on every program run
#========

from turtle import * #fetches turtle commands
from random import * #fetches random number commands
import numpy as np

win = Screen()
win.bgcolor("black") #black background

dna = Turtle(visible=False)
dna.width(2)
dna.speed("fastest")
dna.up()

colors = ["red", "yellow", "purple", "pink", "green", "light blue"] #created a list of colors for the program to choose from

for i in range(randint(1, 150)): #randomizes how many times the loop is run
    dna.color(choice(colors)) #choosing a random color
    dna.goto(randint(-100,100), randint(-100,100)) #choosing a random starting point
    dna.down()
    
    for i in range(randint(1, 100)): #randomizes how long a single line goes for
        dna.forward(50) #all segments are 50 long
        dna.right(randint(-10, 10)*45) #randomizes which angle the turtle turns to, but in multiples of 45 degrees