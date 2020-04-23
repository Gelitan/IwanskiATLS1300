#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:35:27 2020

@author: analiseiwanski

"""

#========
#PC05-Click Game
#Analise Iwanski
#200228
#
#This code creates a game in which there is a dog that must be fed his food
#the player drags the food which is wiggling around the screen to the dog's mouth
#as the player feeds the dog, the score goes up
#========

import pygame, sys, random

# Set up pygame.
pygame.init()

# Set up the window.
WINDOWWIDTH = 720
WINDOWHEIGHT = 500
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),0, 32)
pygame.display.set_caption('please drag slow') #a note to the user that the food will only follow the cursor if dragged slowly

# Set up the colors.
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
LTTAN = (100, 80, 56)
DKTAN = (49, 26, 0)
BLACK = (0,0,0)

x = 370 #center position for all dog parts
y = 370
eye_r = 3 #sets eye radius size
rSize = 1 #sets size and location constant for the dog
FOODSIZE = 20
# Set up the foods
foods = []
for i in range(20): #makes a list of the squares, from , learned from https://inventwithpython.com/invent4thed/chapter19.html
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE),random.randint(0, WINDOWHEIGHT/2 - FOODSIZE), FOODSIZE, FOODSIZE))
score = len(foods) #the score is equal to the number of treats left on the screen

# Set up movement variables.
drag = False

def TextTime(): #learned how to render font on screen from https://kidscancode.org/blog/2016/08/pygame_shmup_part_7/
    font = pygame.font.Font('BebasNeue Bold.otf', 32) #use bebas neue as font that shows the score
    text = font.render('SCORE: '+str(20-score), True, WHITE, BLACK) 
    textRect = text.get_rect()  
    textRect.center = (50, 30) 
    screen.blit(text, textRect)

def mouseFoodClick(mouse): #set up function for when the mouse is inside the area of the food
    for i in range(len(foods)):
        if foods[i].x-FOODSIZE <= mouse[0] <= foods[i].x+FOODSIZE and foods[i].y-FOODSIZE <= mouse[1] <= foods[i].y+FOODSIZE:
            return i

# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drag = True #When mouse is down, the food can be dragged
                        
        elif event.type == pygame.MOUSEMOTION:
            if drag:
                pos = event.pos #update position as mouse moves around
                foodindex = mouseFoodClick(pos)
                if foodindex != None: #if it does not equal None (as long as it is intersecting with a food)
                    foods[foodindex].x = pos[0] #returns the food x position
                    foods[foodindex].y = pos[1] #returns the food y position
                for food in foods[:]:
                    if Head.colliderect(food): #if the food being dragged collides with the dog head area
                        foodindex = mouseFoodClick(pos)
                        if foodindex != None: #if it does not equal None (as long as it is intersecting with a food)
                            foods.remove(foods[foodindex])
                            score -= 1 #remove one from the score (number of treats left on screen)

        elif event.type == pygame.MOUSEBUTTONUP: 
            drag = False #stop dragging food

    screen.fill(WHITE) 
    
    # Draw the dog onto the surface, from the code for the interactive robot
    Body = pygame.draw.polygon(screen, LTTAN, [(int(rSize*(x+65)), int(rSize*(y-35))),(int(rSize*(x+65)),int(rSize*(y+35))), (int(rSize*(x-65)),int(rSize*(y+35))),(int(rSize*(x-65)), int(rSize*(y-35)))])
    Head = pygame.draw.rect(screen,LTTAN,(int(rSize*(x-90)),int(rSize*(y-60)),int(rSize*50),int(rSize*50)))
    Nose = pygame.draw.rect(screen,LTTAN,(int(rSize*(x-105)),int(rSize*(y-35)),int(rSize*20),int(rSize*20)))
    Ear = pygame.draw.rect(screen,DKTAN,(int(rSize*(x-70)),int(rSize*(y-60)),int(rSize*20),int(rSize*30)))
    Eye = pygame.draw.circle(screen, WHITE, (int(rSize*(x-75)), int(rSize*(y-45))),int(rSize*eye_r))
    frontLeg = pygame.draw.rect(screen,DKTAN,(int(rSize*(x-65)),int(rSize*(y+35)),int(rSize*30),int(rSize*50)))
    backLeg = pygame.draw.rect(screen,DKTAN,(int(rSize*(x+35)),int(rSize*(y+35)),int(rSize*30),int(rSize*50)))
    Tail = pygame.draw.polygon(screen, DKTAN, [(int(rSize*(x+65)), int(rSize*(y-35))),(int(rSize*(x+85)),int(rSize*(y-55))), (int(rSize*(x+65)),int(rSize*(y-15)))])

    for i in range(len(foods)): #makes the move wiggle around the screen
        if foods[i].x < 700:
            foods[i].x += random.randint(-5, 5)
        elif foods[i].x >= 700:
            foods[i].x -= random.randint(0, 5)
        if foods[i].y < 480:
            foods [i].y += random.randint(-5, 5)
        elif foods[i].y >= 480:
            foods [i].y -= random.randint(0, 5)
        pygame.draw.rect(screen, LTTAN, foods[i])

    for i in range(len(foods)): #this is for our score, updates how many foods have been fed to the dog
        TextTime()

    # Draw the window onto the screen.
    pygame.display.update()