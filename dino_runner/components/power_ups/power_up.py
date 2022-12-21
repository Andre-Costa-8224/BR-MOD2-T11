import random
from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class PowerUp(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        if self.type == 'shield':
            self.rect.x = SCREEN_WIDTH + random.randint(400, 600)
            self.rect.y = random.randint(125, 175)
        elif self.type == 'sonic':
            self.rect.x = SCREEN_WIDTH + random.randint(500, 700)
            self.rect.y = random.randint(190, 230)
        elif self.type == 'metalcactus':
            self.rect.x = SCREEN_WIDTH + random.randint(595, 795)
            self.rect.y = SCREEN_HEIGHT/1.8
        else:
            self.rect.x = SCREEN_WIDTH + random.randint(400, 600)
            self.rect.y = random.randint(250, 360)

        self.duration = random.randint(5, 10)
        self.start_time = 0

    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            power_ups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)