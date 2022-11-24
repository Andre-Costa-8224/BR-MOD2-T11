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
        self.running = False
        self.deathCount = 0
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = SCREEN_HEIGHT/1.4
        self.points = 0
        self.lastScore = 0
        self.obstacle_manager = ObstacleManager()
        self.player = Dino()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
            
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.points += 1
        self.deathCount += 1
        self.game_speed = 20
        #self.soundTracks()]

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        userInput = pygame.key.get_pressed()
        self.player.update(userInput)
        self.obstacle_manager.update(self)
        if self.points % 100 == 0:
            self.game_speed += 1
        
        self.lastScore = self.points
        
        if self.playing == False:
            self.points = 0

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.screen.blit(self.score(self.points), (SCREEN_WIDTH/1.8, SCREEN_HEIGHT/7))
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

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((255,255,255))
        halfw = SCREEN_WIDTH // 2
        halfh = SCREEN_HEIGHT // 2
        
        if self.deathCount == 0:
            self.textDraw('Press any key to start', halfw, halfh)
        else:
            self.textDraw('Press any key to restart', halfw, halfh)
            self.textDraw(f'SCORE: {self.lastScore}', halfw, halfh+35)
            self.textDraw(f'Deaths: {self.deathCount}', halfw, halfh+70)
            self.screen.blit(ICON, (halfw - 40, halfh - 140))
        
        pygame.display.update()
        self.handle_events_on_menu()

    def textDraw(self, txt, pos_w, pos_h, font = 'Arial'):
        font = pygame.font.SysFont(font, 22, True)
        text = font.render(txt, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (pos_w, pos_h)
        self.screen.blit(text,text_rect)

    def score(self, pontos):
        txtfont = pygame.font.SysFont('Arial', 32, True).render(f'PONTUAÇÃO: {pontos}', True, (0,0,0))
        return txtfont

    def soundTracks(self):
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(SONS_DIR, 'Enemy.mp3'))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.4)