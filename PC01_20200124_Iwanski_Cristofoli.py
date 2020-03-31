#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 09:21:49 2020

@author: analiseiwanski
"""

#========
#PC01-Graffiti
#Analise Iwanski, Ava Cristofoli
#200124
#
#This code creates graffiti on a brick wall that draws a starburst and then spells "POW"
#========

from turtle import * #fetches turtle commands

brickWall = Screen() #create one canvas for all of your turtles.

#You can resize this canvas by using the win.scrensize() command.
#Add a height and width value into the parentheses. For example, 
#if you want a 400x600 window, you'd use (uncommemnt) the next 2 lines:
#win.screensize(400,600)
#win.update()

brickWall.bgcolor('black') #set the canvas color to black
brickWall.bgpic("big-ol-brick-wall.gif") #fill the background with my new brick wall image
brickWall.update() #updates to draw any changes made to the canvas


starburstBlack = Turtle()
starburstBlack.color("black", "black")
starburstBlack.hideturtle()

#moving turtle into starting position
starburstBlack.penup()
starburstBlack.forward(200)
starburstBlack.pendown()
starburstBlack.begin_fill()

#making the starbust
starburstBlack.right(45)
starburstBlack.forward(200)
starburstBlack.right(135)
starburstBlack.forward(200)
starburstBlack.left(90)
starburstBlack.forward(200)
starburstBlack.right(135)
starburstBlack.forward(200)
starburstBlack.left(90)
starburstBlack.forward(200)
starburstBlack.right(135)
starburstBlack.forward(200)
starburstBlack.left(90)
starburstBlack.forward(200)
starburstBlack.right(135)
starburstBlack.forward(200)
starburstBlack.left(90)
starburstBlack.forward(200)
starburstBlack.right(135)
starburstBlack.forward(200)
starburstBlack.left(90)
starburstBlack.forward(200)
starburstBlack.right(135)
starburstBlack.forward(200)
starburstBlack.left(90)
starburstBlack.forward(200)
starburstBlack.right(135)
starburstBlack.forward(200)
starburstBlack.left(90)
starburstBlack.forward(200)
starburstBlack.right(135)
starburstBlack.forward(200)

starburstBlack.end_fill()

#black starburst is complete, time to start on the yellow starburst
starburstYellow = Turtle()
starburstYellow.color("yellow", "yellow")
starburstYellow.hideturtle()

#moving turtle into starting position
starburstYellow.penup()
starburstYellow.forward(180)
starburstYellow.pendown()
starburstYellow.begin_fill()

#making the starbust
starburstYellow.right(45)
starburstYellow.forward(180)
starburstYellow.right(135)
starburstYellow.forward(180)
starburstYellow.left(90)
starburstYellow.forward(180)
starburstYellow.right(135)
starburstYellow.forward(180)
starburstYellow.left(90)
starburstYellow.forward(180)
starburstYellow.right(135)
starburstYellow.forward(180)
starburstYellow.left(90)
starburstYellow.forward(180)
starburstYellow.right(135)
starburstYellow.forward(180)
starburstYellow.left(90)
starburstYellow.forward(180)
starburstYellow.right(135)
starburstYellow.forward(180)
starburstYellow.left(90)
starburstYellow.forward(180)
starburstYellow.right(135)
starburstYellow.forward(180)
starburstYellow.left(90)
starburstYellow.forward(180)
starburstYellow.right(135)
starburstYellow.forward(180)
starburstYellow.left(90)
starburstYellow.forward(180)
starburstYellow.right(135)
starburstYellow.forward(180)

starburstYellow.end_fill()

#both starbursts are complete, next is the letters starting with P
letterP = Turtle()
letterP.color("red")
letterP.hideturtle()
letterP.pensize(20)

#drawing the P
letterP.penup()
letterP.backward(160)
letterP.right(90)
letterP.forward(80)
letterP.right(180)
letterP.pendown()

letterP.forward(150)
letterP.right(90)
letterP.circle(-50, 180) 
#I learned that the first number is the radius, and the second number is the rotation degrees. a negative radius = clockwise turn
#from https://docs.python.org/2/library/turtle.html

#setting up the letter O
letterO = Turtle()
letterO.color("red")
letterO.hideturtle()
letterO.pensize(20)

#drawing the O
letterO.penup()
letterO.left(90)
letterO.forward(70)
letterO.left(90)
letterO.forward(45)
letterO.right(135)
letterO.pendown()

letterO.circle(-45, 90)
letterO.circle(-90,90)
letterO.circle(-45, 90)
letterO.circle(-90,90)
#I read how to draw an oval in Python by combining four different quarter circles with different radii
#from https://pythonturtle.academy/tutorial-drawing-an-oval-with-python-turtle/

#setting up the letter W
letterW = Turtle()
letterW.color("red")
letterW.hideturtle()
letterW.pensize(20)

#drawing the W
letterW.penup()
letterW.forward(60)
letterW.left(90)
letterW.forward(70)
letterW.right(160)
letterW.pendown()

letterW.forward(150)
letterW.left(145)
letterW.forward(75)
letterW.right(145)
letterW.forward(75)
letterW.left(145)
letterW.forward(150)

#stops waiting for new commands and allows you to close out the window
done()