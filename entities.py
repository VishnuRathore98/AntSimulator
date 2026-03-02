import random
import pygame
import math

WIDTH = 800
HEIGHT = 600


class Home:
    def __init__(
        self,
        home_x=WIDTH // 4,
        home_y=HEIGHT // 4,
        home_radius=10,
    ):
        self.home_x = home_x
        self.home_y = home_y
        self.home_radius = home_radius

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (0, 255, 0),
            (int(self.home_x), int(self.home_y)),
            self.home_radius,
        )


class Food:
    def __init__(
        self,
        food_x=WIDTH // 1.5,
        food_y=HEIGHT // 2.5,
        food_radius=10,
        food_quantity=10,
    ):
        self.food_x = food_x
        self.food_y = food_y
        self.food_radius = food_radius
        self.food_quantity = food_quantity

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 0, 0),
            (int(self.food_x), int(self.food_y)),
            self.food_radius,
        )


class Ant:
    def __init__(
        self,
        food: Food,
        ant_x=WIDTH // 2,
        ant_y=HEIGHT // 2,
        ant_angle=random.uniform(0, 2 * math.pi),
        ant_speed=2,
        ant_radius=5,
        ant_home_radius=10,
        ant_state="searching",
        ant_food_x=WIDTH // 1.5,
        ant_food_y=HEIGHT // 2.5,
        ant_food_radius=10,
    ):
        self.ant_x = ant_x
        self.ant_y = ant_y
        self.ant_angle = ant_angle
        self.ant_speed = ant_speed
        self.ant_home_x = ant_x
        self.ant_home_y = ant_y
        self.ant_state = ant_state
        self.ant_radius = ant_radius
        self.ant_home_radius = ant_home_radius
        self.surface_area = HEIGHT * WIDTH
        self.ant_home_area = math.pi * (self.ant_home_radius * self.ant_home_radius)
        self.ant_area = math.pi * (self.ant_radius * self.ant_radius)
        self.ant_food_x = ant_food_x
        self.ant_food_y = ant_food_y
        self.ant_food_radius = ant_food_radius
        self.food = food

    def update(self):
        self.ant_angle += random.uniform(-0.1, 0.1)

        self.ant_x += math.cos(self.ant_angle) * self.ant_speed
        self.ant_y += math.sin(self.ant_angle) * self.ant_speed

        if self.ant_x < 0 or self.ant_x > WIDTH:
            self.ant_angle = math.pi - self.ant_angle
        if self.ant_y < 0 or self.ant_y > HEIGHT:
            self.ant_angle = -self.ant_angle

        # get metrics for food
        diff_sqr_radius = (self.ant_food_radius - self.ant_radius) ** 2
        dist_bw_ant_food = ((self.ant_food_x - self.ant_x) ** 2) + (
            (self.ant_food_y - self.ant_y) ** 2
        )
        sum_sqr_radius = (self.ant_food_radius + self.ant_radius) ** 2

        # get metrics for home
        diff_sqr_radius_home = (self.ant_home_radius - self.ant_radius) ** 2
        dist_bw_ant_home = ((self.ant_home_x - self.ant_x) ** 2) + (
            (self.ant_home_y - self.ant_y) ** 2
        )
        sum_sqr_radius_home = (self.ant_home_radius + self.ant_radius) ** 2

        # Deflaction when touches food logic
        if diff_sqr_radius <= dist_bw_ant_food <= sum_sqr_radius:
            print("touched food!!", int(self.ant_x), int(self.ant_y))
            self.ant_angle = self.ant_angle + math.pi
            # carry food

            self.ant_state = "returning"
            print(self.ant_state)

        if self.ant_state == "returning":
            self.food.food_x = self.ant_x + self.ant_radius
            self.food.food_y = self.ant_y
            # print(f"home=({self.ant_home_x}, {self.ant_home_y})")
            # print(f"ant=({self.ant_x}, {self.ant_y})")
            # Deflaction and drop food when touches home carrying food logic
            if diff_sqr_radius_home <= dist_bw_ant_home <= sum_sqr_radius_home:
                print("touched home!!", int(self.ant_x), int(self.ant_y))
                # put food
                self.food.food_x = self.ant_x
                self.food.food_y = self.ant_y
                self.ant_state = "searching"
                self.ant_angle = self.ant_angle + math.pi
                print(self.ant_state)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(self.ant_x), int(self.ant_y)),
            self.ant_radius,
        )
