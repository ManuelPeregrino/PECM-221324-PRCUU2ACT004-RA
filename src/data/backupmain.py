import pygame
import sys

from models.belt import Belt
from models.square import Square
from views.background import Background
from models.floor import Floor
from controllers.music import MusicPlayer

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
        self.create_belts()
        self.direction = 0
        self.current_belt_layer = self.belts_layer_1
        self.square = Square(10, 10)
        self.square2 = Square(100,10)
        self.moving_sprites.add(self.square)
        self.moving_sprites.add(self.square2)
        self.background = Background()


    def create_belts(self):
        # Create belts and add them to the moving_sprites group
        self.belts_layer_1 = [Belt(x * 30 + 10, 100) for x in range(30)]
        self.belts_layer_2 = [Belt(x * 30 + 400, 200) for x in range(30)]
        self.belts_layer_3 = [Belt(x * 30 + 20, 300) for x in range(30)]
        self.floor_layer = [Floor(x * 30 + 0, 800) for x in range(50)]

        for belt in self.belts_layer_1 + self.belts_layer_2 + self.belts_layer_3+self.floor_layer:
            self.moving_sprites.add(belt)
        
    def run(self):
        while True:
            self.handle_events()
            # Update each belt
            speed = 0.4 # Adjust speed as necessary
            for belt in self.belts_layer_1 + self.belts_layer_2 + self.belts_layer_3+self.floor_layer:
                belt.update(speed)
                Square.update(self.square, self.belts_layer_1+self.belts_layer_2+self.belts_layer_3+self.floor_layer)
                Square.update(self.square2, self.belts_layer_1+self.belts_layer_2+self.belts_layer_3+self.floor_layer)
   
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
