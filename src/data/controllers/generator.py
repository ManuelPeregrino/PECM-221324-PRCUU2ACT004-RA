import pygame
import random
from models.square import Square  # Ensure this import matches your project structure
from models.barrel import Barrel
from models.garbage import Garbage
class Generator:
    def __init__(self, screen_width):
        self.screen_width = screen_width
        self.last_square_generation_time = pygame.time.get_ticks()
        self.square_generation_interval = self.random_interval()
        self.last_barrel_generation_time = pygame.time.get_ticks()
        self.barrel_generation_interval = self.random_interval()
        self.last_garbage_generation_time = pygame.time.get_ticks()
        self.garbage_generation_interval = self.random_interval()

    def random_interval(self):
        return random.randint(1000, 5000)  # Random interval between 1 and 3 seconds

    def garbage_interval(self):
        return random.randint(1000,6000)
    
    def create_square(self):
        pos_x = 90  # Randomize starting X position
        pos_y = 10  # Start from the top of the screen
        return Square(pos_x, pos_y)

    def create_barrel(self):
        pos_x = 130  # Randomize starting X position
        pos_y = 10  # Start from the top of the screen
        return Barrel(pos_x, pos_y)  # Assuming Square takes position and size

    def create_garbage(self):
        pos_generator=random.randint(0,1)
        if pos_generator == 1:
            pos_x = 130  # Randomize starting X position
            pos_y = 10  # Start from the top of the screen
        else:
            pos_x = 90  # Randomize starting X position
            pos_y = 10  # Start from the top of the screen
                     
        return Garbage(pos_x, pos_y)  # Assuming Square takes position and size
             
    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_square_generation_time > self.square_generation_interval:
            new_square = self.create_square()
            self.last_square_generation_time = current_time
            self.square_generation_interval = self.random_interval()
            return new_square
        
        if current_time - self.last_barrel_generation_time > self.barrel_generation_interval:
            self.barrel_generation_interval = self.random_interval()
            self.last_barrel_generation_time = current_time
            new_barrel = self.create_barrel()
            return new_barrel
        
        if current_time - self.last_garbage_generation_time > self.garbage_generation_interval:
            self.garbage_generation_interval = self.random_interval()
            self.last_garbage_generation_time = current_time
            new_garbage = self.create_garbage()
            return new_garbage
        
        return None