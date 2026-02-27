import random
import pygame
import math
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Ant Simulator")

clock = pygame.time.Clock()


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

    def update(self):
        self.ant_angle += random.uniform(-0.1, 0.1)

        self.ant_x += math.cos(self.ant_angle) * self.ant_speed
        self.ant_y += math.sin(self.ant_angle) * self.ant_speed

        if self.ant_x < 0 or self.ant_x > WIDTH:
            self.ant_angle = math.pi - self.ant_angle
        if self.ant_y < 0 or self.ant_y > HEIGHT:
            self.ant_angle = -self.ant_angle

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(self.ant_x), int(self.ant_y)),
            5,
        )


# Creating a colony of ants
ants = [Ant() for i in range(10)]

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

    pygame.display.flip()

pygame.quit()
sys.exit()
