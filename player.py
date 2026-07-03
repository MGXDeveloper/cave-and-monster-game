import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Player:
    def __init__(self, x, y):
        self.image_right = pygame.image.load("image/player_right.png").convert_alpha()
        self.image_right = pygame.transform.scale(self.image_right, (50, 50))

        self.image_left = pygame.image.load("image/player_left.png").convert_alpha()
        self.image_left = pygame.transform.scale(self.image_left, (50, 50))

        self.image = self.image_right
        self.x = x
        self.y = y
        self.coins_collected = 0
        self.hitbox = pygame.Rect(self.x, self.y, 50, 50)
        self.key = False

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self, direction):
        if direction == "left":
            if self.x - 60 > 0:
                self.x -= 60
                self.image = self.image_left
        elif direction == "right":
            if self.x + 60 < SCREEN_WIDTH:
                self.x += 60
                self.image = self.image_right
        elif direction == "up":
            if self.y - 55 > 0:
                self.y -= 55
        elif direction == "down":
            if self.y + 55 < SCREEN_HEIGHT:
                self.y += 55

        self.hitbox.topleft = (self.x, self.y)
