#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 09:35:27 2020

@author: analiseiwanski

"""

#========
#PC10-APIs
#Analise Iwanski and Madison Aeling
#200410
#
#This code uses a sunrise/sunset API and time data to create an adjusting bar that shows the current time,
#time of sunrise, time of sunset, time of solar noon, day length, and an image associated with the time of day
#========

import pygame
from random import * #imports all the random functions so we can use them.
import numpy as np # math library
import urllib #accesses online data
import json #processes online data
import requests
import pdb
from datetime import datetime, timedelta, tzinfo #import datetime

pygame.init()

#set up our screen (global variables)
screen = pygame.display.set_mode((1000,800)) 
screen.fill((255,255,255))
pygame.init()
clock = pygame.time.Clock()
moonimage = pygame.image.load(("Moon.gif")) #nighttime image
sunrisesunsetimage = pygame.image.load(("SunsetSunrise.gif")) #sunrise/sunset image
sunimage = pygame.image.load(("Sun.gif")) #daytime image

#import sunrise/sunset data for Boulder, CO
sun = requests.get('http://api.sunrise-sunset.org/json?lat=40.014984&lng=-105.270546&date=2020-04-10')
sun_json  = sun.json()

#convert API data into datetime objects
sunrise = datetime.strptime(sun_json['results']['sunrise'], '%X %p') - timedelta(hours=6)
sunset = datetime.strptime(sun_json['results']['sunset'], '%X %p') - timedelta(hours=6)
solarNoon = datetime.strptime(sun_json['results']['solar_noon'], '%X %p') - timedelta(hours=18)
dayLength = datetime.strptime(sun_json['results']['day_length'], '%X')
now = datetime.now()

#turn times into strings to be printed
NowString = str(now.time())
SunriseString = str(sunrise.time())
SunsetString = str(sunset.time())
SolarNoonString = str(solarNoon.time())
DayLengthString = str(dayLength.time())

font = pygame.font.SysFont("DINAlternateBold.ttf", 20) #sets up text to be printed

#set up the text to render on the screen
currentText = font.render('Current Time: ' + NowString[0:8], True, (0, 0, 0))
sunriseText = font.render('Sunrise: ' + SunriseString[0:9], True, (0, 0, 0))
sunsetText = font.render('Sunset: ' + SunsetString[0:9], True, (0, 0, 0))
solarNoonText = font.render('Solar Noon: ' + SolarNoonString[0:9], True, (0, 0, 0))
dayLengthText = font.render('Day Length: ' + DayLengthString[0:9] + ' hours', True, (0, 0, 0))

def daytimeMeasure():
    '''Function prints the text and adjusts the time bars/locations when it is daytime hours'''
    screen.blit(currentText, (50,50))
    pygame.draw.rect(screen,(0,0,0),(50,100,(now.hour *40),20))
    screen.blit(sunriseText, (50,150))
    pygame.draw.rect(screen,(255,0,0),(50,90,10,40))
    screen.blit(sunsetText, ((sunset.hour *40),150))
    pygame.draw.rect(screen,(255,0,0),((sunset.hour *40),90,10,40))
    screen.blit(solarNoonText, ((solarNoon.hour *40),150))
    pygame.draw.rect(screen,(255,0,0),((solarNoon.hour *40),90,10,40))
    screen.blit(dayLengthText, (50,200))
    
def nighttimeMeasure():
    '''Function prints the text and adjusts the time bars/locations when it is nighttime hours'''
    screen.blit(currentText, (50,50))
    pygame.draw.rect(screen,(0,0,0),(50,100,((now.hour-12)*40),20))
    screen.blit(sunriseText, (((sunrise.hour+12)*40),150))
    pygame.draw.rect(screen,(255,0,0),(((sunrise.hour+12)*40),90,10,40))
    screen.blit(sunsetText, (50,150))
    pygame.draw.rect(screen,(255,0,0),(50,90,10,40))

while True: #main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    
    screen.fill((255, 255, 255)) #make screen white

    if sunset.time()>= now.time() >= sunrise.time(): #if it is daytime, execute function and display sun
        daytimeMeasure()
        screen.blit(sunimage, [350,200])
    elif now.time() == sunset.time(): #if it is sunset, execute function and display sunset
        nighttimeMeasure()
        screen.blit(sunrisesunsetimage, [600,200])
    elif now.time() == sunrise.time(): #if it is sunset, execute function and display sunrise
        daytimeMeasure()
        screen.blit(sunrisesunsetimage, [600,200])
    else: #if it is nighttime, execute function and display moon
        nighttimeMeasure()
        screen.blit(moonimage, [350,200])
    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
