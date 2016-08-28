import pygame, sys, time
from pygame.locals import *

pygame.init()

FPS=30
fpsClock=pygame.time.Clock()

width=400
height=300
DISPLAYSURF=pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('Animation')
background=pygame.image.load('bg.png')


UP='up'
LEFT='left'
RIGHT='right'
DOWN='down'
SPACE='space'

boom_s = pygame.mixer.Sound("boom.wav")
sprite=pygame.image.load('ship.gif')
spritex=200
spritey=130
direction=None

def move(direction, sprite, spritex, spritey):
    if direction:
        if direction == K_UP:
            spritey-=5
            #sprite=pygame.image.load('up.png')
        elif direction == K_DOWN:
            spritey+=5
            #sprite=pygame.image.load('down.png')
        if direction == K_LEFT:
            spritex-=5
            #sprite=pygame.image.load('left.png')
        elif direction == K_RIGHT:
            spritex+=5
            #sprite=pygame.image.load('right.png')
    return sprite, spritex, spritey

#pygame.mixer.music.load('bgm.mp3')
#pygame.mixer.music.play(-1, 0.0)
while True:
    DISPLAYSURF.blit(background,(0,0))

    DISPLAYSURF.blit(sprite,(spritex,spritey))

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        if keys[K_SPACE]:
            boom_s.play()
        if event.type == KEYDOWN:
            direction = event.key
        if event.type == KEYUP:
            if (event.key == direction):
                direction = None
    sprite, spritex, spritey = move(direction, sprite, spritex, spritey)

    pygame.display.update()
    fpsClock.tick(FPS)
