from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Obstacle(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = SCREEN_HEIGHT/1.45

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:
            obstacles.pop()
        if self.type > 2:
            self.rect.y = SCREEN_HEIGHT/1.74

    def draw(self, screen):
        screen.blit(self.image[self.type], (self.rect.x, self.rect.y))
