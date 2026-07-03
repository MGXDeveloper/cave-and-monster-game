import pygame


class Door:
    def __init__(self, x, y):
        self.image = pygame.image.load("image/door.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x, self.y, 50, 50)
        self.collected = False

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
