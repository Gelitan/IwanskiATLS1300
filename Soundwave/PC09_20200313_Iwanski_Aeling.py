#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:35:27 2020

@author: analiseiwanski

"""

#========
#PC08-Soundwave
#Analise Iwanski and Madison Aeling
#200317
#
#This code makes concentric circles that appear randomly around the screen that look like ripples
#The ripples appear in beat to the music that plays when the code is run
#========

import pygame, sys
from random import * #fetches random number commands
from pygame.locals import *
import time
pygame.init()

pygame.mixer.music.load('Xylo-Ziko02-Phase_2.wav') #loading the music
pygame.mixer.music.play(0) #play the music from the beginning
song = pygame.mixer.Sound('Xylo-Ziko02-Phase_2.wav') 
song.set_volume(0.4) #set sound volume

pywindow = pygame.display.set_mode((500, 500)) #setting up the window

#defining colors
WHITE = (255, 255, 255)
BLUE = (51, 51, 255)
BLUETWO = (132, 132, 255)
BLUETHREE = (181, 181, 255)
RED = (201, 25, 12)
REDTWO = (217, 94, 84)
REDTHREE = (228, 142, 135)

pywindow.fill(WHITE)
clock = pygame.time.Clock() #used for the timing of the music with the ripples
timer1sec = 0

#defining elements of the ripples
r = [30,40,50] #first circles' radii
rtwo = [60,70,80] #second circles' radii
i = 0
circ_x = randint(0,500)  #first circles' x location
circ_y = randint(0,500) #first circles' y location
circ_x2 = randint(0,500) #second circles' x location
circ_y2 = randint(0,500) #second circles' y location
color = [BLUE, BLUETWO, BLUETHREE] #first circles' colors
colortwo = [RED, REDTWO, REDTHREE] #second circles' colors


def draw_myshape(r,circ_x,circ_y,color):
        """this function creates the blue ripples in the animation"""
        circle = pygame.draw.circle(pywindow, color, (circ_x,circ_y), r, 1)
        pygame.display.update(circle)
        
def draw_myshapetwo(rtwo,circ_x2,circ_y2,colortwo):
        """this function creates the red, larger ripples in the animation"""
        circle = pygame.draw.circle(pywindow, colortwo, (circ_x2,circ_y2), rtwo, 1)
        pygame.display.update(circle)

while True: #main game loop

    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            run = False    
    if time.time() - timer1sec >= 0.34:   # if half a second passes
        draw_myshape(r[i],circ_x,circ_y,color[i])  #draw blue ripples
        draw_myshapetwo(rtwo[i],circ_x2,circ_y2,colortwo[i]) #draw red ripples
        timer1sec = time.time()
        i += 1 #cycle through the indices
        if i == 3: #reset the indices after three cyles
            circ_x = randint(0,500) 
            circ_y = randint(0,500)
            circ_x2 = randint(0,500) 
            circ_y2 = randint(0,500)
            i = 0
            pywindow.fill(WHITE)
         
    clock.tick(30)
