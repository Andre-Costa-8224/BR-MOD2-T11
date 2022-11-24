from random import randrange
import pygame
from pygame.locals import *
from dino_runner.utils.constants import SCREEN_WIDTH, CLOUD

class Clouds(pygame.sprite.Sprite):
    def __init__(self):
        self.w = SCREEN_WIDTH
        pygame.sprite.Sprite.__init__(self)
        self.image = CLOUD
        self.rect = self.image.get_rect()
        self.rect.y = randrange(50,200,50)
        self.rect.x = randrange(SCREEN_WIDTH-50,SCREEN_WIDTH+100,50)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = self.w
            self.rect.y = randrange(50,200,60)
        self.rect.x -= 5