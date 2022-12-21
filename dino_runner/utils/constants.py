import pygame
import os

# Global Constants
TITLE = "Crazy Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 700
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
SONS_DIR = os.path.join(os.path.dirname(__file__),"..", "assets/sons")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SONIC = [
    pygame.image.load(os.path.join(IMG_DIR, "Sonic/sonicRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Sonic/sonicRun2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Sonic/sonicRun3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Sonic/sonicRun4.png"))
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Shield.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer1.png")),
]

RUNNING_ROBOT = []

for c in range(2,4):
    img = pygame.image.load(os.path.join(IMG_DIR, f"Robot/robo{c}.png"))
    RUNNING_ROBOT.append(pygame.transform.scale(img, (32*4, 32*4)))

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))
JUMPING_SONIC = pygame.image.load(os.path.join(IMG_DIR, 'Sonic/sonicAppear.png'))
JUMPING_ROBOT = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Robot/robo1.png")), (32*4, 32*4))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Shield.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Hammer.png")),
]

DUCKING_SONIC = [
    pygame.image.load(os.path.join(IMG_DIR, 'Sonic/sonicDuck1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Sonic/sonicDuck2.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Sonic/sonicDuck3.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Sonic/sonicDuck4.png'))
]

DINO_DEAD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead.png"))

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]

LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
SONIC = pygame.image.load(os.path.join(IMG_DIR, 'Sonic/sonicAppear.png'))
METALCACTUS = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'Cactus/metalcactus.png')), (40*3.3,40*3))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = 'hammer'
SONIC_TYPE = 'sonic'
METALCACTUS_TYPE = 'metalcactus'