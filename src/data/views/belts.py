import pygame

from models.belt import Belt

class Belts():
    
    def create_belts(self):
        # Create belts and add them to the moving_sprites group
        self.belts_layer_1 = [Belt(x * 30 + 10, 90) for x in range(25)]
        self.belts_layer_2 = [Belt(x * 30 + 400, 180) for x in range(16)]
        self.belts_layer_3 = [Belt(x * 30 + 20, 500) for x in range(15)]

        for belt in self.belts_layer_1 + self.belts_layer_2 + self.belts_layer_3:
            self.moving_sprites.add(belt)