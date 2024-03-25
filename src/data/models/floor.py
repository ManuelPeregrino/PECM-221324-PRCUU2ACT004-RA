import pygame
import sys

class Floor(pygame.sprite.Sprite):
    floor_images = [
        pygame.image.load('src/assets/sprites/Custom/barrel_sprite.png'),
        pygame.image.load('src/assets/sprites/Tiles/IndustrialTile_57.png'),
        pygame.image.load('src/assets/sprites/Tiles/IndustrialTile_56.png')
    ]

    def __init__(self, pos_x, pos_y,direction=0):
        super().__init__()
        self.is_animating = False
        self.image = Floor.floor_images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.direction = direction


