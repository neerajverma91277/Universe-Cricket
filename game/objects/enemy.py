from math import cos, pi, sin
from random import randint, randrange
from typing import Tuple

from pygame.transform import rotate
from pygame.sprite import Sprite, spritecollide, collide_rect
from pygame import Rect, Surface

from config.constants import (
    BULLET_GROUP,
    ENEMY_GROUP,
    ENEMY_INITIAL_SPEED,
    ENEMY_SPEED_THRESHOLD,
    INVERSE_SHOOT_DIFICULTY,
)
from .duo import Shooter
from .groups import groups
from utils.responsive import Responsive


class Enemy(Sprite):
    """
    Enemy Sprite\n
    Moves around in a circle in random order\n
    Reverses direction on collision with similar enemy
    """

    def __init__(self, angle: float, player: Shooter):
        from config.assets import enemy

        super().__init__(groups[ENEMY_GROUP])

        self.angle = angle
        initial_direction = randint(-1, 1)

        self.player = player

        self.clean_image: Surface = enemy
        self.image = rotate(self.clean_image, (3 * pi / 2 - self.angle) * (180 / pi))
        self.rect: Rect = self.image.get_rect(center=self.calculate_position())
        self.speed = ENEMY_INITIAL_SPEED * initial_direction

    def update_speed(self) -> float:
        speed = self.speed

        acceleration = randrange(-1, 1) / 5000
        speed += acceleration

        if abs(self.speed) >= ENEMY_SPEED_THRESHOLD:
            speed = -speed / 2

        group = groups[ENEMY_GROUP].copy()
        group.remove(self)
        if spritecollide(self, group, False):
            speed = -speed

        return speed

    def update(self):
        super().update()
        self.speed = self.update_speed()
        self.angle += self.speed
        self.angle = self.angle % (2 * pi)
        self.image = rotate(self.clean_image, (3 * pi / 2 - self.angle) * (180 / pi))
        self.rect: Rect = self.image.get_rect(center=self.calculate_position())
        if (randint(0, 100000)) % INVERSE_SHOOT_DIFICULTY == 0:
            self.shoot()

    def shoot(self):
        from .bullet import Bullet

        # Enemy rect center
        self_position = self.calculate_position()
        x = self_position[0]
        y = self_position[1]

        # Player rect center
        shooter_position = self.player.calculate_position()
        a = shooter_position[0]
        b = shooter_position[1]

        diag = ((x - a) ** 2 + (y - b) ** 2) ** 0.5
        shoot_angle_cosine = (x - a) / diag
        shoot_angle_sine = (y - b) / diag
        Bullet(shoot_angle_cosine, shoot_angle_sine, self.angle, self)

    def calculate_position(self) -> Tuple[float, float]:
        return (
            Responsive.center()[0] + Responsive.Enemy.circle_radius() * cos(self.angle),
            Responsive.center()[1] + Responsive.Enemy.circle_radius() * sin(self.angle),
        )
