import pygame
from pygame.locals import *
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, SONS_DIR, DEFAULT_TYPE
from dino_runner.components.dino import Dino
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.clouds import Clouds
from random import randrange
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
        self.x_pos_cloud = randrange(SCREEN_WIDTH-50, SCREEN_WIDTH+100, 50)
        self.y_pos_cloud = randrange(50,150,50)
        self.cloudSprites = pygame.sprite.Group()

        for c in range(3):
            self.cloudSprites.add(Clouds())

        self.points = 0
        self.lastScore = 0
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.player = Dino()
        self.pause = False

    def execute(self):
        self.running = True
        soundTracks('Enemy.mp3')
        while self.running:
            if not self.playing:
                self.show_menu()
            
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        while self.playing:
            self.events()
            if self.pause:
                self.showMusicMenu()
            else:
                self.update()
            self.draw()
            self.points += 1
        self.deathCount += 1
        self.game_speed = 20

    def events(self):
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if key[K_1]:
                soundTracks('Enemy.mp3')
                self.pause = False
            elif key[K_2]:
                self.pause = False
                soundTracks('ImSoSorry.mp3')
            elif key[K_3]:
                soundTracks('GiornosTheme.mp3')
                self.pause = False
            elif key[K_ESCAPE]:
                self.pause = True
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        userInput = pygame.key.get_pressed()
        self.player.update(userInput)
        self.obstacle_manager.update(self)
        self.cloudSprites.update()
        self.power_up_manager.update(self.points, self.game_speed, self.player)

        if self.points % 100 == 0:
            self.game_speed += 1
        
        self.lastScore = self.points
        
        if self.playing == False:
            self.player.dead()
            self.points = 0

    def draw(self):
        if self.pause:
            self.clock.tick(FPS)
        else:
            self.clock.tick(FPS)
            self.screen.fill((255, 255, 255))
            self.draw_background()
            self.draw_clouds()
            self.player.draw(self.screen)
            self.obstacle_manager.draw(self.screen)
            self.screen.blit(self.score(), (SCREEN_WIDTH/1.9, SCREEN_HEIGHT/7))
            self.draw_power_up_time()
            self.power_up_manager.draw(self.screen)
            pygame.display.update()
            pygame.display.flip()

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                self.textDraw(
                    f"{self.player.type.capitalize()} enabled for {time_to_show} seconds",
                    SCREEN_WIDTH/2.5,
                    30
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_clouds(self):
        self.cloudSprites.draw(self.screen)

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
            self.textDraw('(Press ESC while playing shows music options)', halfw, halfh+30)
        else:
            pygame.time.wait(1000)
            self.textDraw('Press any key to restart', halfw, halfh)
            self.textDraw('(Press ESC while playing shows music options)', halfw, halfh+100)
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

    def score(self):
        txt = pygame.font.SysFont('Arial', 32, True).render(f'PONTUAÇÃO: {self.lastScore}', True, (0,0,0))
        return txt

    def showMusicMenu(self):
        self.textDraw('PRESS 1 to play Enemy and return', SCREEN_WIDTH/2, SCREEN_HEIGHT/3)
        self.textDraw('PRESS 2 to play Im So Sorry and return', SCREEN_WIDTH/2, SCREEN_HEIGHT/2.6)
        self.textDraw("PRESS 3 to play Giorno's Theme and return", SCREEN_WIDTH/2, SCREEN_HEIGHT/2.3)
        pygame.display.update()
        self.handle_events_on_pause()

    def handle_events_on_pause(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False


def soundTracks(opt):
    pygame.mixer.music.load(os.path.join(SONS_DIR, opt))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)
