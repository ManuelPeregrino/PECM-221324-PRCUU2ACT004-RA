import pygame
import sys

class Belt(pygame.sprite.Sprite):
    def __init__(self, pos_x,pos_y):
        super().__init__()
        self.is_animating=False
        self.test_conveyor_belt = []
        self.test_conveyor_belt.append(pygame.image.load('src/assets/sprites/Animated_Objects/Transporter1.png').convert_alpha())
        self.test_conveyor_belt.append(pygame.image.load('src/assets/sprites/Animated_Objects/Transporter2.png').convert_alpha())
        self.test_conveyor_belt.append(pygame.image.load('src/assets/sprites/Animated_Objects/Transporter3.png').convert_alpha())
        self.current_belt = 0
        self.image = self.test_conveyor_belt[self.current_belt]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def animate(self):
        self.is_animating=True

    def stop_animate(self):
        self.is_animating=False

    def update(self, speed):
        if self.is_animating == True:
            self.current_belt += speed

            if self.current_belt >= len(self.test_conveyor_belt):
                self.current_belt = 0

                

            self.image=self.test_conveyor_belt[int(self.current_belt)]


pygame.init()
clock = pygame.time.Clock()

screen_width = 600
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('ReFactory')

moving_sprites = pygame.sprite.Group()
conveyor=Belt(100,100)
conveyor2=Belt(250,100)
moving_sprites.add(conveyor)
moving_sprites.add(conveyor2)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                conveyor.animate()
                conveyor2.animate()
            if event.key == pygame.K_d:
                conveyor.animate()
                conveyor2.animate()
                        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                conveyor.stop_animate()
                conveyor2.stop_animate()
            if event.key == pygame.K_d:
                conveyor.stop_animate()
                conveyor2.stop_animate()

    screen.fill((0,0,0))
    moving_sprites.draw(screen)
    moving_sprites.update(0.15)
    pygame.display.flip()
    clock.tick(144)