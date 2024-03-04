import pygame
import sys

from views.belts import Belt
from views.square import Square
from data.map import Background

class Main:

    pygame.init()
    clock = pygame.time.Clock()
    screen_width = 600
    screen_height = 400
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('ReFactory')

    def __init__(self):

        self.moving_sprites = pygame.sprite.Group()
        self.create_belts()
        self.direction = 0
        self.current_belt_layer = self.belts_layer_1
        self.square = Square(10, 10)
        self.moving_sprites.add(self.square)
        self.background = Background()

    def create_belts(self):
        # Create belts and add them to the moving_sprites group
        self.belts_layer_1 = [Belt(x * 30 + 10, 90) for x in range(10)]
        self.belts_layer_2 = [Belt(x * 30 + 100, 180) for x in range(10)]
        self.belts_layer_3 = [Belt(x * 30 + 420, 270) for x in range(2)]
        
        for belt in self.belts_layer_1 + self.belts_layer_2 + self.belts_layer_3:
            self.moving_sprites.add(belt)

    def run(self):
        while True:
            self.handle_events()
            # Update each belt
            speed = 0.25  # Adjust speed as necessary
            for belt in self.belts_layer_1 + self.belts_layer_2 + self.belts_layer_3:
                belt.update(speed)
                Square.update(self.square, self.belts_layer_1+self.belts_layer_2+self.belts_layer_3)
            self.draw()
            self.clock.tick(60)  # Limit the frame rate to 60 FPS


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_a]:  # Example keys to start animation
                    for belt in self.belts_layer_1 + self.belts_layer_2 + self.belts_layer_3:
                        belt.animate()
                        belt.direction=-1
                if event.key in [pygame.K_d]:  # Example keys to start animation
                    for belt in self.belts_layer_1 + self.belts_layer_2 + self.belts_layer_3:
                        belt.animate()
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_a, pygame.K_d]:  # Stop animation when these keys are released
                    for belt in self.belts_layer_1 + self.belts_layer_2 + self.belts_layer_3:
                        belt.stop_animate()



    def update(self):
        # Update the game state here
        pass

    def draw(self):
        self.screen.fill((0,0,0))
        self.background.draw(self.screen)
        self.moving_sprites.draw(self.screen)
        pygame.display.flip()
        

if __name__ == '__main__':
    game = Main()
    game.run()
