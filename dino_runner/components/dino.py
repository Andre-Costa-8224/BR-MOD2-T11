from pygame.locals import *
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, SCREEN_HEIGHT, DINO_DEAD, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, HAMMER_TYPE, DUCKING_HAMMER, JUMPING_HAMMER, RUNNING_HAMMER, RUNNING_SONIC, DUCKING_SONIC, JUMPING_SONIC, SONIC_TYPE, RUNNING_ROBOT, JUMPING_ROBOT, METALCACTUS_TYPE

JUMP_SPEED = 8.5

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER, SONIC_TYPE: DUCKING_SONIC, METALCACTUS_TYPE: RUNNING_ROBOT}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER, SONIC_TYPE: JUMPING_SONIC, METALCACTUS_TYPE: JUMPING_ROBOT}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER, SONIC_TYPE: RUNNING_SONIC, METALCACTUS_TYPE: RUNNING_ROBOT}



class Dino(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.index = 0
        self.rect = self.image.get_rect()
        self.y = SCREEN_HEIGHT/1.5
        self.rect.x = 80

        self.jumping = False
        self.ducking = False
        self.jump_level = JUMP_SPEED
        self.jumpDown = False
        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.show_text = False
        self.power_time_up = 0

    def run(self):
        self.index += 0.25
        if self.index > 1 and self.type != 'sonic':
            self.index = 0
        elif self.index > 3 and self.type == 'sonic':
            self.index = 0
        elif self.index > 3 and self.type != 'sonic':
            self.index = 0
        

        self.image = RUN_IMG[self.type][int(self.index)]
            

    def update(self, key):
        if self.jumping == False:
            self.run()
            if self.ducking and self.type != 'metalcactus':
                self.duck()
            else:
                self.rect.y = self.y-50
        elif self.jumping:
            self.jump()
            if key[K_DOWN]:
                self.jumpDown = True
        
        if self.type == "sonic":
            self.y += 5
        else:
            self.y = SCREEN_HEIGHT/1.5

        if self.type == 'metalcactus':
            self.y -= 18
        else:
            self.y = SCREEN_HEIGHT/1.5

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
        self.index += 0.25

        if self.index > 1 and self.type != 'sonic':
            self.index = 0
        elif self.index > 3 and self.type == 'sonic':
            self.index = 0
        elif self.index > 3 and self.type != 'sonic':
            self.index = 0
        
        self.rect.y = self.y-11
        self.ducking = False
        self.image = DUCK_IMG[self.type][int(self.index)]

    def dead(self):
        self.image = DINO_DEAD
        if self.ducking:
            self.rect.y = self.y-50
        return self.image

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))