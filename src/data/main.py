import pygame
import sys

from models.belt import Belt
from views.background import Background
from models.floor import Floor
from models.walls import Walls
from controllers.music import MusicPlayer
from controllers.generator import Generator

class Main:

    pygame.init()
    clock = pygame.time.Clock()
    screen_width = 1440
    screen_height = 900
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('ReFactory')

    def __init__(self):

        self.music_player = MusicPlayer('src/assets/sounds/Talking.ogg')
        self.music_player.start()  # Start music playback
        self.moving_sprites = pygame.sprite.Group()
        self.static_sprites = pygame.sprite.Group()
        self.create_belts()
        self.direction = 0
        self.current_belt_layer = self.belts_layer_1
        self.generator = Generator(screen_width=1440)

        self.background = Background()


    def create_belts(self):
        # Create belts and add them to the moving_sprites group
        self.belts_layer_1 = [Belt(x * 30 + 10, 100) for x in range(15)]
        self.belts_layer_2 = [Belt(x * 30 + 480, 100) for x in range(15)]
        self.belts_layer_3 = [Belt(x * 30 + 100, 300) for x in range(15)]
        
        self.packed_belts = self.belts_layer_1 +  self.belts_layer_2 +  self.belts_layer_3
        
        for belt in self.packed_belts:
            self.moving_sprites.add(belt)

    def run(self):
        while True:

            new_object = self.generator.update()

            if new_object:
                self.moving_sprites.add(new_object)
            self.handle_events()
    
            # Update each belt
            speed = 1 # Adjust speed as necessary

            for Square in self.moving_sprites:
                for belt in self.packed_belts:
                    Square.update(self.packed_belts)
                belt.update(speed)


            self.moving_sprites.draw(self.screen)

            self.draw()
            self.clock.tick(60)  # Limit the frame rate to 60 FPS

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.music_player.stop() 
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_a]:  # Example keys to start animation
                    for belt in self.packed_belts:
                        belt.animate()
                        belt.direction=-1
                if event.key in [pygame.K_d]:  # Example keys to start animation
                    for belt in self.packed_belts:
                        belt.animate()
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_a, pygame.K_d]:  # Stop animation when these keys are released
                    for belt in self.packed_belts:
                        belt.stop_animate()

    def update(self):
        # Update the game state here
        pass

    def draw(self):
        self.screen.fill((0,0,0))
        self.background.draw(self.screen)
        self.moving_sprites.draw(self.screen)
        self.static_sprites.draw(self.screen)
        pygame.display.flip()
        

if __name__ == '__main__':
    game = Main()
    game.run()
