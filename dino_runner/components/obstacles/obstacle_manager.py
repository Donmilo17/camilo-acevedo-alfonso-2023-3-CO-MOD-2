import pygame
import random
from dino_runner.components.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, SHIELD_TYPE, HAMMER_TYPE

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        # Add obstacle to list
        if len(self.obstacles) == 0:
            obstacle = self.generate_obstacle_image(random.randint(0, 2))
            self.obstacles.append(obstacle)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            # pygame.time.delay(100)
            # print(game.player.dino_rect.colliderect(obstacle.rect))
            if game.player.dino_rect.colliderect(obstacle.rect):
                #Controlar si el dino tiene shield o no
                if game.player.type == SHIELD_TYPE:
                    game.playing = False
                    game.death_count.update()
                    break
                else:
                    self.obstacles.remove(obstacle)
            if game.hammer.rect.colliderect(obstacle.rect):
                game.hammer.flag_hammer = False
                self.obstacles.remove(obstacle)


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def generate_obstacle_image(self, obstacle_type):
        if obstacle_type == 0:
            obstacle = Cactus('SMALL')
        elif obstacle_type == 1:
            obstacle = Cactus('LARGE')
        else:
            obstacle = Bird()

        return obstacle

    def reset_obstacles(self):
        self.obstacles = []
        