import pygame
import sys

class Belt(pygame.sprite.Sprite):
    test_conveyor_belt_images = [
        pygame.image.load('src/assets/sprites/Tiles/IndustrialTile_74.png'),
        pygame.image.load('src/assets/sprites/Tiles/IndustrialTile_75.png'),
        pygame.image.load('src/assets/sprites/Tiles/IndustrialTile_76.png')
    ]

    def __init__(self, pos_x, pos_y, direction=0):
        super().__init__()
        self.is_animating = False
        self.current_belt = 0
        self.image = Belt.test_conveyor_belt_images[self.current_belt]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.direction = direction  # Added attribute for direction (and speed)

    def animate(self):
        self.is_animating = True
        self.direction=0.5

    def stop_animate(self):
        self.is_animating = False
        self.direction=0

    def update(self, speed):
        if self.is_animating:
            self.current_belt = (self.current_belt + speed) % len(Belt.test_conveyor_belt_images)
            self.image = Belt.test_conveyor_belt_images[int(self.current_belt)]
