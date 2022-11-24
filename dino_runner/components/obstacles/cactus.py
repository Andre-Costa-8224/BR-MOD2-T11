import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SCREEN_HEIGHT

class Cactus(Obstacle):
    def __init__(self, image: list):
        self.type = random.randint(0, 5)
        super().__init__(image, self.type)
        self.rect.y = SCREEN_HEIGHT/1.62
        if self.type > 2:
            self.rect.y = SCREEN_HEIGHT/1.74

