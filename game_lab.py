import pygame
import random
import math

from pygame.locals import *

pygame.init()


class Star(pygame.sprite.Sprite):

    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([1, 1])

        self.rect = self.image.get_rect()
        self.rect = self.rect.move([random.randint(0, size[0]), random.randint(0, size[1])])

        self.size = size

        self.move = random.randint(5, 25)
        self.current = self.move

    def update(self, screen):
        self.current -= 1
        if self.current == 0:
            self.current = self.move
            self.rect = self.rect.move(-1, 0)

        self.brightness = random.randint(100-self.move*4, 255-self.move*4)
        self.image.fill([self.brightness, self.brightness, self.brightness])

        if self.rect.right < 0:
            self.rect = self.rect.move(self.size[0], 0)

        screen.blit(self.image, self.rect)


class Pixel(pygame.sprite.Sprite):

    def __init__(self, size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("ship.gif")
        self.rect = self.image.get_rect()

        self.rect = self.rect.move(size[0]/8, size[1]/2)

        self.speed = 4

    def update(self, screen, keys, size):

        # move
        if keys[K_UP]:
            self.rect = self.rect.move(0, -self.speed)
        if keys[K_DOWN]:
            self.rect = self.rect.move(0, self.speed)
        if keys[K_LEFT]:
            self.rect = self.rect.move(-self.speed, 0)
        if keys[K_RIGHT]:
            self.rect = self.rect.move(self.speed, 0)

        # bounce
        if self.rect.top < 0:
            self.rect = self.rect.move(0, self.speed)
        if self.rect.bottom > size[1]:
            self.rect = self.rect.move(0, -self.speed)
        if self.rect.left < 0:
            self.rect = self.rect.move(self.speed, 0)
        if self.rect.right > size[0]:
            self.rect = self.rect.move(-self.speed, 0)

        # render
        screen.blit(self.image, self.rect)


pygame.mouse.set_visible(False)

size = (800, 600)
time = 0
stars = []
for star in xrange(100):
    stars.append(Star(size))

screen = pygame.display.set_mode(size, 32)
pixel = Pixel(size)


while True:
    time += 1
    keys = pygame.key.get_pressed()
