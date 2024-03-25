import pygame
import sys


class Barrel(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()  # Call the parent class (Sprite) constructor
        self.image = pygame.image.load('src/assets/sprites/Objects/Barrel1.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.drop_to_next_level = False
        self.velocity_y = 1  # Initial vertical velocity
        self.update_counter = 0  # Counter to control update frequency
        self.update_frequency = 15  # Update every 5 frames        
    def update(self, belts, gravity=2):
        self.update_counter += 1
        if self.update_counter >= self.update_frequency:
            self.update_counter = 0

        # Apply gravity
            self.rect.y += self.velocity_y

        # Check for collision with any belt
        belt_hit_list = pygame.sprite.spritecollide(self, belts, False)
        if belt_hit_list:
            # If colliding with a belt, stop the fall and adjust the square's position to sit on the belt
            self.rect.bottom = belt_hit_list[0].rect.top
            self.velocity_y = 0  # Reset vertical velocity
            self.drop_to_next_level = False  # No longer needs to drop
            
            if self.update_counter == 0:
                # Move along with the belt's direction
                self.rect.x += belt_hit_list[0].direction
        else:
            # If not colliding, continue to apply gravity
            self.velocity_y = gravity
            self.drop_to_next_level = False  # Set to drop until it lands on the next belt
