import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load the background image
        self.sky_surface = pygame.image.load('src/assets/sprites/Background/Background.png').convert()
        self.sky_surface = pygame.transform.scale(self.sky_surface, (1440, 900))
   
        # Optionally scale the image to fit the screen or desired size
        # For example, to scale to 800x600, you can uncomment the next line

        
        self.rect = self.sky_surface.get_rect()
        self.rect.left, self.rect.top = 0, 0

    def draw(self, screen):
        screen.blit(self.sky_surface, self.rect)
