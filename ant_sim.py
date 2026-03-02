import os
import sys
import pygame
from entities import Ant, Food, Home

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Ant Simulator")

clock = pygame.time.Clock()

ant_svg_path = os.path.abspath("./assets/ant.svg")
food_svg_path = os.path.abspath("./assets/food.svg")
home_svg_path = os.path.abspath("./assets/home.svg")

ant_svg = pygame.image.load(ant_svg_path)


home = Home()

# Creating multiple food items
foods = [Food(food_radius=5) for i in range(10)]

# Creating a colony of ants
ants = [
    Ant(
        food=foods[i],
        ant_x=home.home_x,
        ant_y=home.home_y,
        ant_food_x=foods[i].food_x,
        ant_food_y=foods[i].food_y,
        ant_speed=5,
    )
    for i in range(10)
]


running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    home.draw(screen)

    for food in foods:
        food.draw(screen)

    for ant in ants:
        ant.update()
        ant.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
