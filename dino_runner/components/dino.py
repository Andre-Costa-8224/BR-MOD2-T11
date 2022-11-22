import pygame
from dino_runner.utils.constants import RUNNING

class Dino():
    def __init__(self):
        self.imgdinolist = RUNNING
        self.index = 0
        self.image = self.imgdinolist[self.index]
        self.rect = self.image.get_rect()
        self.y = 310
        self.rect.center = (80, 360)
        self.pulo = False

    def update(self):
        if self.index > 1:
            self.index = 0
        self.index += 0.25
        self.image = self.imgdinolist[int(self.index)]
        if self.pulo == True:
            if self.rect.y <= 120:
                self.pulo = False
            self.rect.y -= 20
        else:
            if self.rect.y < self.y:
                self.rect.y += 20
            else:
                self.rect.y = self.y

    def pular(self):
        self.pulo = True

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))