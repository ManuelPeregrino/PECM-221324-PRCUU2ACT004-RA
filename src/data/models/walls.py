import pygame
import sys

class Walls(pygame.sprite.Sprite):
    wall_images = [
        pygame.image.load('src/assets/sprites/Tiles/IndustrialTile_55.png'),
        pygame.image.load('src/assets/sprites/Tiles/IndustrialTile_57.png'),
        pygame.image.load('src/assets/sprites/Tiles/IndustrialTile_56.png')
    ]

    def __init__(self, pos_x, pos_y,direction=0):
        super().__init__()
        self.is_animating = False
        self.image = Walls.wall_images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.direction = direction


