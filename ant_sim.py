import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

ant_x = 100
ant_y = 300

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Ant Simulator")

clock = pygame.time.Clock()

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ant_x += 2

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (255, 255, 255), (ant_x, ant_y), 5)

    pygame.display.flip()

pygame.quit()
sys.exit()
