import pygame as p
from pygame.locals import *
import cv2 as cv
import numpy as np
import sys

p.init()
width=720
height=480
Window =p.display.set_mode((width,height),1,16)
p.display.set_caption("Polaris")

redColor = p.Color(255,0,0)
blackColor = p.Color(255,0,0)

white = (0, 0, 255)
black = (0, 0, 0)
font = p.font.SysFont('Garamond', 30)
text = font.render('Timeline', False, (255, 0, 0))



backGround = p.image.load('space.png')
backGround = p.transform.scale(backGround,(width,height))


x = 0
widthR=5
heightR=50
p.draw.rect(Window,redColor,Rect(x,height/2,widthR,heightR))

a = x
size_of_gas_cloud = 30

path='/Users/hany/Desktop/nasa'
name='variant.png'

while True:
    img = cv.imread('star.png',cv.IMREAD_UNCHANGED)
    if p.mouse.get_pressed()[0] != 0:
        a = p.mouse.get_pos()[0] - 5
        if a < x:
            a = x
        elif a>255:
            a=255
    if a<=55:
        brightness=a+200
    elif a<=110:
        brightness=255-(a-55)
    elif a<=165:
        brightness=200+(a-110)
    else:
        brightness=255-(a-165)
    cal=img
    brightness = brightness + 50
    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))
    if brightness != 0:

        if brightness > 0:

            shadow = brightness

            max = 255

        else:

            shadow = 0
            max = 255 + brightness

        al_pha = (max - shadow) / 255
        ga_mma = shadow
        cal = cv.addWeighted(img, al_pha,
                              img, 0, ga_mma)
    Window.blit(text, (300,80))
    cv.imwrite(name,cal)
    star = p.image.load(name)
    star = p.transform.scale(star,(320,320))
    Window.blit(backGround,(0,0))
    Window.blit(star,(360,80))
    # p.draw.rect(Window, blackColor, Rect(0, 0, width, height))
    p.draw.rect(Window, redColor, Rect(a, height/2, widthR, heightR))
    p.display.update()
    for event in p.event.get():
       if event.type == QUIT:
          p.quit()
          sys.exit()
       elif event.type == KEYDOWN:
          if event.key == K_ESCAPE:
             p.quit()