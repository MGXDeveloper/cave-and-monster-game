import pygame
import random
import tkinter as tk
from tkinter import messagebox
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, X_RANGE, Y_RANGE
from player import Player
from monster import Monster
from monster_bad_wind import MonsterBadWind
from coin import Coin
from hole import Hole, HoleWind
from door import Door
from key import Key


def show_popup(title, message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title, message)
    root.destroy()


pygame.init()

screen_width = SCREEN_WIDTH
screen_height = SCREEN_HEIGHT
screen = pygame.display.set_mode((screen_width, screen_height))

game_title = "My Pygame Window"
pygame.display.set_caption(game_title)

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

background_image = pygame.image.load("background2.png")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

player = Player(6, 2)

monster = Monster(random.choice(X_RANGE), random.choice(Y_RANGE))

monster_bad_winds = []
for _ in range(2):
    offset_x = random.randint(-60, 60)
    offset_y = random.randint(-55, 55)
    bad_wind = MonsterBadWind(monster.x + offset_x, monster.y + offset_y)
    bad_wind.offset_x = offset_x
    bad_wind.offset_y = offset_y
    monster_bad_winds.append(bad_wind)

door = Door(random.choice(X_RANGE), 550)

key = Key(random.choice(X_RANGE), random.choice(Y_RANGE))

coins = [Coin(random.choice(X_RANGE), random.choice(Y_RANGE)) for _ in range(10)]

holes = [Hole(random.choice(X_RANGE), random.choice(Y_RANGE)) for _ in range(3)]

hole_winds = []
for h in holes:
    for _ in range(2):
        hole_wind = HoleWind(h.x + random.randint(-60, 60), h.y + random.randint(-55, 55))
        hole_winds.append(hole_wind)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move("left")
            elif event.key == pygame.K_RIGHT:
                player.move("right")
            elif event.key == pygame.K_UP:
                player.move("up")
            elif event.key == pygame.K_DOWN:
                player.move("down")
            monster.move()

            for bad_wind in monster_bad_winds:
                bad_wind.collected = False
                bad_wind.visible = False
                bad_wind.move(monster.x, monster.y)

    screen.fill((0, 255, 0))
    screen.blit(background_image, (0, 0))

    door.draw(screen)
    key.draw(screen)

    for c in coins:
        c.draw(screen)

    player.draw(screen)
    monster.draw(screen)

    for bad_wind in monster_bad_winds:
        bad_wind.draw(screen)

    for h in holes:
        h.draw(screen)

    for hw in hole_winds:
        hw.draw(screen)

    for c in coins:
        if player.hitbox.colliderect(c.hitbox) and not c.collected:
            c.visible = True
            c.collected = True
            player.coins_collected += 1
            print(f"Coins collected: {player.coins_collected}")

    for h in holes:
        if player.hitbox.colliderect(h.hitbox):
            h.visible = True
            pygame.display.flip()
            show_popup("Game Over", "You fell into a hole!")
            print("Game Over! You fell into a hole.")
            running = False

    for hw in hole_winds:
        if player.hitbox.colliderect(hw.hitbox) and not hw.collected:
            hw.visible = True
            hw.collected = True
            pygame.display.flip()
            show_popup("Game Over", "You were blown away by the wind!")
            print("Game Over! You were blown away by the wind.")

    if player.hitbox.colliderect(key.hitbox) and not key.collected:
        key.visible = True
        key.collected = True
        player.key = True
        show_popup("Key Collected", "You have collected the key!")
        print("Key collected!")

    if player.hitbox.colliderect(door.hitbox):
        if player.key:
            door.collected = True
            show_popup("Congratulations!", "You have unlocked the door and won the game!")
            print("Congratulations! You have unlocked the door and won the game.")
            running = False
        else:
            if not door.collected:
                door.collected = True
                show_popup("Door Locked", "You need to collect the key to unlock the door!")
                print("Door is locked! You need to collect the key to unlock it.")

    if player.hitbox.colliderect(monster.hitbox):
        show_popup("Game Over", "You were caught by the monster!")
        print("Game Over! You were caught by the monster.")
        running = False

    for bad_wind in monster_bad_winds:
        if player.hitbox.colliderect(bad_wind.hitbox) and not bad_wind.collected:
            bad_wind.visible = True
            bad_wind.collected = True
            pygame.display.flip()
            show_popup("Game Over", "You were blown away by the monster's bad wind!")
            print("Game Over! You were blown away by the monster's bad wind.")

    pygame.display.flip()
