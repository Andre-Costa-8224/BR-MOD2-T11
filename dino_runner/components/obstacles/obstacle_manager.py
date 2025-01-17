from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from random import choice


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(choice([Cactus(SMALL_CACTUS+LARGE_CACTUS), Bird()]))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    game.playing = False
                    break
                else:
                    if game.player.type == 'hammer':
                        self.obstacles.remove(obstacle)
                    elif game.player.type == 'sonic':
                        self.obstacles.remove(obstacle)
                        game.points += 20
                    pass

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
        