from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
from random import choice

class Bird(Obstacle):
    def __init__(self):
        super().__init__(BIRD, 0)
        self.rect.y = choice((250, 300, 360))
        self.index = 0
    
    def draw(self, screen):
        screen.blit(self.image[int(self.index)], self.rect)
        self.index += 0.25

        if self.index > 1:
            self.index = 0