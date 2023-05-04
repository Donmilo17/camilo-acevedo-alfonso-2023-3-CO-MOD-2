import random
import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class Powerup(sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(125, 175)
        self.start_time = 0
        
    def update (self, game_speed, powerups):
        #configurando la animacion del powerup de derecha a izquierda
        self.rect.x -= game_speed 
        #eliminando powerup 
        if self.rect.x < -self.rect.width:
            powerups.pop()
        
    def draw(self, screen):
        screen.blit(self.image, (200, 300))