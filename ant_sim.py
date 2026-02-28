import random
import pygame
import math
import sys
import os

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


class Ant:
    def __init__(
        self,
        ant_x=WIDTH // 2,
        ant_y=HEIGHT // 2,
        ant_angle=random.uniform(0, 2 * math.pi),
        ant_speed=2,
    ):
        self.ant_x = ant_x
        self.ant_y = ant_y
        self.ant_angle = ant_angle
        self.ant_speed = ant_speed
        self.ant_home_x = ant_x
        self.ant_home_y = ant_y

    def update(self):
        self.ant_angle += random.uniform(-0.1, 0.1)

        self.ant_x += math.cos(self.ant_angle) * self.ant_speed
        self.ant_y += math.sin(self.ant_angle) * self.ant_speed

        if self.ant_x < 0 or self.ant_x > WIDTH:
            self.ant_angle = math.pi - self.ant_angle
        if self.ant_y < 0 or self.ant_y > HEIGHT:
            self.ant_angle = -self.ant_angle

        # Deflaction when touches home logic
        if self.ant_x == self.ant_home_x or self.ant_y == self.ant_home_y:
            self.ant_angle = self.ant_angle + math.pi

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(self.ant_x), int(self.ant_y)),
            5,
        )


class Food:
    def __init__(self, food_x=WIDTH // 1.5, food_y=HEIGHT // 2.5):
        self.food_x = food_x
        self.food_y = food_y

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 0, 0),
            (int(self.food_x), int(self.food_y)),
            10,
        )


class Home:
    def __init__(self, home_x=WIDTH // 4, home_y=HEIGHT // 4):
        self.home_x = home_x
        self.home_y = home_y

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (0, 255, 0),
            (int(self.home_x), int(self.home_y)),
            10,
        )


home = Home()

# Creating a colony of ants
ants = [Ant(ant_x=home.home_x, ant_y=home.home_y) for i in range(10)]

food = Food()


running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for ant in ants:
        ant.update()
        ant.draw(screen)

    food.draw(screen)

    home.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
