import pygame


class Hole:
    def __init__(self, x, y):
        self.image = pygame.image.load("image/hole.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x, self.y, 50, 50)
        self.visible = False

    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, (self.x, self.y))


class HoleWind:
    def __init__(self, x, y):
        self.image = pygame.image.load("image/hole_wind.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x, self.y, 50, 50)
        self.visible = False
        self.collected = False

    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, (self.x, self.y))
