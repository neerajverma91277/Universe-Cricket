from typing import Optional

import pygame

from utils.responsive import Responsive

background: Optional[pygame.Surface] = None
bullet: Optional[pygame.Surface] = None
catcher: Optional[pygame.Surface] = None
duo_circle: Optional[pygame.Surface] = None
enemy: Optional[pygame.Surface] = None
enemy_circle: Optional[pygame.Surface] = None
shooter: Optional[pygame.Surface] = None
earth: Optional[pygame.Surface] = None
planet0: Optional[pygame.Surface] = None
spacecraft0: Optional[pygame.Surface] = None
spaceship: Optional[pygame.Surface] = None
planet1: Optional[pygame.Surface] = None
planet2: Optional[pygame.Surface] = None
gradient: Optional[pygame.Surface] = None
rock0: Optional[pygame.Surface] = None
rock1: Optional[pygame.Surface] = None


def init_assets():
    global background, bullet, catcher, duo_circle, enemy, enemy_circle, shooter, earth, planet0, spacecraft0, spaceship, planet1, planet2, gradient, rock0, rock1
    background = pygame.image.load("assets/background.png").convert_alpha()
    bullet = pygame.transform.scale(
        pygame.image.load("assets/bullet.png").convert_alpha(),
        (Responsive.Bullet.size(),) * 2,
    )
    catcher = pygame.transform.scale(
        pygame.image.load("assets/catcher.png").convert_alpha(),
        (Responsive.Player.size(),) * 2,
    )
    duo_circle = pygame.transform.scale(
        pygame.image.load("assets/duo_circle.png").convert_alpha(),
        (2 * Responsive.Player.circle_radius(),) * 2,
    )
    enemy = pygame.transform.scale(
        pygame.image.load("assets/enemy.png").convert_alpha(),
        (Responsive.Enemy.size(),) * 2,
    )
    enemy_circle = pygame.transform.scale(
        pygame.image.load("assets/enemy_circle.png").convert_alpha(),
        (2 * Responsive.Enemy.circle_radius(),) * 2,
    )
    shooter = pygame.transform.scale(
        pygame.image.load("assets/shooter.png").convert_alpha(),
        (1.5 * Responsive.Player.size(),) * 2,
    )
    earth = pygame.transform.scale(
        pygame.image.load("assets/earth.png").convert_alpha(),
        (Responsive.Player.circle_radius(),) * 2,
    )
    planet0 = pygame.transform.scale(
        pygame.image.load("assets/planet0.png").convert_alpha(),
        (2.5 * Responsive.Player.circle_radius(),) * 2,
    )
    spacecraft0 = pygame.transform.scale(
        pygame.image.load("assets/spacecraft0.png").convert_alpha(),
        (Responsive.Player.circle_radius(),) * 2,
    )
    # spaceship
    spaceship_image = pygame.image.load("assets/spaceship.png")
    width = Responsive.Player.circle_radius() * 1.5
    height = width * spaceship_image.get_height() / spaceship_image.get_width()
    spaceship = pygame.transform.scale(spaceship_image, (width, height))
    # planet1
    planet1_image = pygame.image.load("assets/planet1.png").convert_alpha()
    width = Responsive.Player.circle_radius()
    height = width * planet1_image.get_height() / planet1_image.get_width()
    planet1 = pygame.transform.scale(planet1_image, (width, height))
    # planet2
    planet2_image = pygame.image.load("assets/planet2.png").convert_alpha()
    width = Responsive.Player.circle_radius()
    height = width * planet2_image.get_height() / planet2_image.get_width()
    planet2 = pygame.transform.scale(planet2_image, (width, height))
    # gradient
    gradient_image = pygame.image.load("assets/gradient.png").convert_alpha()
    width = Responsive.Player.circle_radius() * 4
    height = width * gradient_image.get_height() / gradient_image.get_width()
    gradient = pygame.transform.scale(gradient_image, (width, height))
    # rock0
    rock0_image = pygame.image.load("assets/rock0.png").convert_alpha()
    width = Responsive.Player.circle_radius()
    height = width * rock0_image.get_height() / rock0_image.get_width()
    rock0 = pygame.transform.scale(rock0_image, (width, height))
    # rock1
    rock1_image = pygame.image.load("assets/rock1.png").convert_alpha()
    width = Responsive.Player.circle_radius() * 1.5
    height = width * rock1_image.get_height() / rock1_image.get_width()
    rock1 = pygame.transform.scale(rock1_image, (width, height))
