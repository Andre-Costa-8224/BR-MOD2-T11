from pygame.locals import *
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, SCREEN_HEIGHT

JUMP_SPEED = 8.5

class Dino(Sprite):
    def __init__(self):
        self.imgdinolist = RUNNING
        self.index = 0
        self.image = self.imgdinolist[self.index]
        self.rect = self.image.get_rect()
        self.y = SCREEN_HEIGHT/1.5
        self.rect.center = (80, self.y)
        self.pulo = False
        self.agachar = False
        self.jump_level = JUMP_SPEED

    def run(self):
        self.index += 0.25
        self.image = self.imgdinolist[int(self.index)]

        if self.index > 1:
            self.index = 0

    def update(self, key):

        if self.pulo == False:
            self.run()
            if self.agachar == True:
                self.duck()
            else:
                self.rect.y = self.y-50
        elif self.pulo:
            self.jump()
            if key[K_DOWN]:
                self.agachar = False
                self.jump_level -= 0.8

        if (key[K_SPACE] or key[K_UP]) and self.pulo == False:
            self.pulo = True
            self.agachar = False
        elif key[K_DOWN] and self.pulo == False:
            self.agachar = True
            self.pulo = False

    def jump(self):
        self.image = JUMPING
        if self.pulo == True:
            self.rect.y -= self.jump_level * 4
            self.jump_level -= 0.8

        if self.jump_level < -JUMP_SPEED:
            self.rect.y = self.y-50
            self.pulo = False
            self.jump_level = JUMP_SPEED
    
    def duck(self):
        self.image = DUCKING[int(self.index)]
        self.index += 0.25

        if self.index > 1:
            self.index = 0
        
        self.rect.y = self.y-6
        self.agachar = False

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))