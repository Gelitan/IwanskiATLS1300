#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 09:41:11 2020

@author: analiseiwanski
"""

#========
#PC02-Animating with Turtles
#Analise Iwanski
#200131
#
#This code creates an abstract animation of tangent circles with radii based on the fibonacci sequence, then creates a red and blue 
#opposite strings of semicircles to make a strand of DNA
#========

from turtle import * #fetches turtle commands
import numpy as np #from Dr. Z's programming mathematical equations doc

window = Screen()
window.setup(800, 800, 100, 100) #setting up the window
window.bgcolor("black")

circleWhite = Turtle() #naming and creating the first turtle
circleWhite.color("white")
circleWhite.shape("triangle")
circleWhite.turtlesize(0.5)
circleWhite.pensize(3)
circleWhite.penup()
circleWhite.speed(10)


fibonacciNumbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144] #got list of fibonnaci numbers from https://www.mathsisfun.com/numbers/fibonacci-sequence.html

numberOfNumbers=len(fibonacciNumbers) #gives value of the length of the list, learned from https://www.geeksforgeeks.org/find-size-of-a-ist-in-python/

circleWhite.pendown()

#use for loops to create circles for the number of fibonnaci numbers
for i in range(numberOfNumbers):
    circleWhite.circle(fibonacciNumbers[i],360)
    
#use for loops to create circles for the number of fibonnaci numbers, but mirrored horizontally
for i in range(numberOfNumbers):
    circleWhite.circle(-fibonacciNumbers[i],360)

halfCircleRed = Turtle() #creating second turtle
halfCircleRed.color("red")
halfCircleRed.shape("turtle")
halfCircleRed.turtlesize(0.5)
halfCircleRed.pensize(3)
halfCircleRed.penup()
halfCircleRed.speed(8)
halfCircleRed.goto(-300,0)


halfCircleRed.pendown()
halfCircleRed.left(90)

evens = [0,2,4,6,8,10,12,14]
odds = [1,3,5,7,9,11,13,15]

#drawing the animation to create the red semicircles
for h in range(15): #chose 15 as the number of semicircles, created semicircles that face opposite by creating different rule for evens and odds
    if h in evens:
        halfCircleRed.right(180)
        halfCircleRed.circle(20,180)
    if h in odds:
        halfCircleRed.left(180)
        halfCircleRed.circle(20,-180)

halfCircleBlue = Turtle() #creating third turtle
halfCircleBlue.color("blue")
halfCircleBlue.shape("turtle")
halfCircleBlue.turtlesize(0.5)
halfCircleBlue.pensize(3)
halfCircleBlue.penup()
halfCircleBlue.speed(8)
halfCircleBlue.goto(300,0)


halfCircleBlue.pendown()
halfCircleBlue.right(90)

evens = [0,2,4,6,8,10,12,14]
odds = [1,3,5,7,9,11,13,15]

#drawing the animation to create the blue semicircles
for k in range(15):
    if k in evens:
        halfCircleBlue.right(180)
        halfCircleBlue.circle(20,180)
    if k in odds:
        halfCircleBlue.left(180)
        halfCircleBlue.circle(20,-180)
