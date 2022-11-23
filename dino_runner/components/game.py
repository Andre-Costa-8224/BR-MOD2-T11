import pygame
from pygame.locals import *
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, SONS_DIR
from dino_runner.components.dino import Dino
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

import os

class Game:
    def __init__(self):

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = SCREEN_HEIGHT/1.4
        self.points = 0
        self.obstacle_manager = ObstacleManager()
        self.player = Dino()

        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(SONS_DIR, 'Enemy.mp3'))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.4)


    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.points += 1
        self.soundTracks()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        userInput = pygame.key.get_pressed()
        self.player.update(userInput)
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.screen.blit(self.pontuation(self.points), (SCREEN_WIDTH/1.8, SCREEN_HEIGHT/7))
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def pontuation(self, pontos):
        txtfont = pygame.font.SysFont('Arial', 32, True).render(f'PONTUAÇÃO: {pontos}', True, (0,0,0))
        return txtfont

    def soundTracks(self):
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(SONS_DIR, 'Enemy.mp3'))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.4)