import random

import pygame

from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:

    def __init__(self):
        self.obstacles = []


    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))

            elif random.randint(0, 2) == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS))

            elif random.randint(0, 2) == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    if game.life_manager.life_counter()==1:
                        pygame.time.delay(500)
                        game.death_count += 1
                        game.playing = False
                        game.previus_points = game.points
                        game.points = 0
                        break
                else:
                    game.life_manager.delete_life()

                self.obstacles.remove(obstacle)


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []