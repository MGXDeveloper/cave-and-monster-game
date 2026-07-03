import pygame


class Coin:
    def __init__(self, x, y):
        self.image = pygame.image.load("image/coin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x, self.y, 30, 30)
        self.visible = False
        self.collected = False

    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, (self.x, self.y))
