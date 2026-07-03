import pygame


class MonsterBadWind:
    def __init__(self, x, y):
        self.image = pygame.image.load("image/monster_badwind.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x, self.y, 50, 50)
        self.visible = False
        self.collected = False

    def move(self, monster_x, monster_y):
        target_x = monster_x + self.offset_x
        target_y = monster_y + self.offset_y

        if self.x < target_x:
            self.x += 60
        elif self.x > target_x:
            self.x -= 60

        if self.y < target_y:
            self.y += 55
        elif self.y > target_y:
            self.y -= 55

        self.hitbox.topleft = (self.x, self.y)

    def draw(self, screen):
        if self.visible:
            screen.blit(self.image, (self.x, self.y))
