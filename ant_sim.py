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

ant1_x = WIDTH // 2
ant1_y = HEIGHT // 2
ant1_angle = random.uniform(0, 2 * math.pi)
ant1_speed = 2

ant2_x = WIDTH // 2
ant2_y = HEIGHT // 2
ant2_angle = random.uniform(0, 2 * math.pi)
ant2_speed = 2

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # ant 1
    ant1_angle += random.uniform(-0.1, 0.1)

    ant1_x += math.cos(ant1_angle) * ant1_speed
    ant1_y += math.sin(ant1_angle) * ant1_speed

    if ant1_x < 0 or ant1_x > WIDTH:
        ant1_angle = math.pi - ant1_angle
    if ant1_y < 0 or ant1_y > HEIGHT:
        ant1_angle = -ant1_angle

    pygame.draw.circle(screen, (255, 255, 255), (int(ant1_x), int(ant1_y)), 5)

    # ant 2
    ant2_angle += random.uniform(-0.1, 0.1)

    ant2_x += math.cos(ant2_angle) * ant2_speed
    ant2_y += math.sin(ant2_angle) * ant2_speed

    if ant2_x < 0 or ant2_x > WIDTH:
        ant2_angle = math.pi - ant2_angle
    if ant2_y < 0 or ant2_y > HEIGHT:
        ant2_angle = -ant2_angle

    pygame.draw.circle(screen, (255, 255, 255), (int(ant2_x), int(ant2_y)), 5)

    pygame.display.flip()

pygame.quit()
sys.exit()
