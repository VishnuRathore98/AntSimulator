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

ant_x = WIDTH // 2
ant_y = HEIGHT // 2
ant_angle = random.uniform(0, 2 * math.pi)
ant_speed = 2

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ant_angle += random.uniform(-0.1, 0.1)

    ant_x += math.cos(ant_angle) * ant_speed
    ant_y += math.sin(ant_angle) * ant_speed

    if ant_x < 0 or ant_x > WIDTH:
        ant_angle = math.pi - ant_angle
    if ant_y < 0 or ant_y > HEIGHT:
        ant_angle = -ant_angle

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (255, 255, 255), (int(ant_x), int(ant_y)), 5)

    pygame.display.flip()

pygame.quit()
sys.exit()
