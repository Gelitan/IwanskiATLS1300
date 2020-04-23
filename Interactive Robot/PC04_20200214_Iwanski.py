#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:35:27 2020

@author: analiseiwanski

"""

#========
#PC04-Interactice Robot
#Analise Iwanski
#200214
#
#This code creates a dog in a living room who can respond to key and mouse functions
#He can jump when the user holds down spacebar, move left and right with arrow keys, and grow with mouse click
#========

import pygame
from random import *
import time

pygame.init() #initializes all pygame functions

size = 720
screen = pygame.display.set_mode((720,480)) #create 720 x 480 pixel screen

bg = pygame.image.load(("livingroom.gif")) #import living room image from https://www.deviantart.com/nhe1/art/Living-Room-459587347
screen.blit(bg, [0, 0]) #setting background as image https://www.pygame.org/docs/ref/surface.html?highlight=blit#pygame.Surface.blit

#set up RGB colors
LTTAN = (82, 72, 55)
DKTAN = (74, 56, 33)
BLACK = (0,0,0)
WHITE = (255,255,255)

Run = True
x = size/2 #center position for all dog parts
y = 370
scale = 1 #variable to adjust when keys are pressed to change size of dog
speed = 5
eye_r = 3 #radius of the eye
rSize = 1 #sets size and location constant for the dog
goingUp = True #makes going up and down as part of jump

#Game loop
while Run:
    time.sleep(.03)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            Run = False
            
    keys = pygame.key.get_pressed() #this section tells the dog to go left and right with left and right key presses      
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_LEFT]:
        x -= speed
        
    if keys[pygame.K_SPACE]: #this section tells the dog to go up on spacebar press and back down upon hitting a certain height
        if y<=300:
            goingUp = False
        if y >= 300 and goingUp:
            y -= speed
        elif y <= 370 and not goingUp:
            y+=speed
        
    mouse = pygame.mouse.get_pressed() #this section tells the dog to grow with mouse click
    if mouse[0]:
        if rSize <=1: 
            rSize *= 1.1 #increases size of dog
        elif rSize > 1:
            rSize /= 1.1 #decreases size of dog

    screen.blit(bg, [0, 0]) #makes sure dogs aren't drawn on top of each other

    #drawing the dog! includes adjustments for size/position  
    #Pygame draw docs: https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
    Body = pygame.draw.polygon(screen, LTTAN, [(int(rSize*(x+65)), int(rSize*(y-35))),(int(rSize*(x+65)),int(rSize*(y+35))), (int(rSize*(x-65)),int(rSize*(y+35))),(int(rSize*(x-65)), int(rSize*(y-35)))])
    Head = pygame.draw.rect(screen,LTTAN,(int(rSize*(x-90)),int(rSize*(y-60)),int(rSize*50),int(rSize*50)))
    Nose = pygame.draw.rect(screen,LTTAN,(int(rSize*(x-105)),int(rSize*(y-35)),int(rSize*20),int(rSize*20)))
    Ear = pygame.draw.rect(screen,DKTAN,(int(rSize*(x-70)),int(rSize*(y-60)),int(rSize*20),int(rSize*30)))
    Eye = pygame.draw.circle(screen, WHITE, (int(rSize*(x-75)), int(rSize*(y-45))),int(rSize*eye_r))
    frontLeg = pygame.draw.rect(screen,DKTAN,(int(rSize*(x-65)),int(rSize*(y+35)),int(rSize*30),int(rSize*50)))
    backLeg = pygame.draw.rect(screen,DKTAN,(int(rSize*(x+35)),int(rSize*(y+35)),int(rSize*30),int(rSize*50)))
    Tail = pygame.draw.polygon(screen, DKTAN, [(int(rSize*(x+65)), int(rSize*(y-35))),(int(rSize*(x+85)),int(rSize*(y-55))), (int(rSize*(x+65)),int(rSize*(y-15)))])
    

    pygame.display.update() #update all changes to screen
    