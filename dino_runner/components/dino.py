from pygame.locals import *
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, SCREEN_HEIGHT, DINO_DEAD, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, HAMMER_TYPE, DUCKING_HAMMER, JUMPING_HAMMER, RUNNING_HAMMER

JUMP_SPEED = 8.5

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}



class Dino(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.index = 0
        self.rect = self.image.get_rect()
        self.y = SCREEN_HEIGHT/1.5
        self.rect.center = (80, self.y)
        self.jumping = False
        self.ducking = False
        self.jump_level = JUMP_SPEED
        self.jumpDown = False
        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0

    def run(self):
        self.image = RUN_IMG[self.type][int(self.index)]
        self.index += 0.25

        if self.index > 1:
            self.index = 0

    def update(self, key):
        if self.jumping == False:
            self.run()
            if self.ducking:
                self.duck()
            else:
                self.rect.y = self.y-50
        elif self.jumping:
            self.jump()
            if key[K_DOWN]:
                self.jumpDown = True
        

        if (key[K_SPACE] or key[K_UP]) and self.jumping == False:
            self.ducking = False
            self.jumping = True
        elif key[K_DOWN] and not self.jumping:
            self.jumping = False
            self.ducking = True

    def jump(self):
        self.image = JUMP_IMG[self.type]
        self.rect.y -= self.jump_level * 4
        self.jump_level -= 0.8

        """
        if self.jumpDown:
            self.rect.y -= self.jump_level * 4
            self.jumpDown = False
        """

        if self.jump_level < -JUMP_SPEED:
            self.rect.y = self.y-50
            self.jumping = False
            self.jump_level = JUMP_SPEED
    
    def duck(self):
        self.image = DUCK_IMG[self.type][int(self.index)]
        self.index += 0.25

        if self.index > 1:
            self.index = 0
        
        self.rect.y = self.y-11
        self.ducking = False

    def dead(self):
        self.image = DINO_DEAD
        if self.ducking:
            self.rect.y = self.y-50
        return self.image

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))