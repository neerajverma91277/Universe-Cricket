from math import cos, sin
from pygame import Rect, Surface
from pygame.sprite import Sprite, spritecollide, collide_rect
from typing import Tuple, Union

from config.constants import BULLET_GROUP, BULLET_VELOCITY, ENEMY_GROUP
from .groups import groups
from .duo import Shooter
from .enemy import Enemy
from utils.responsive import Responsive


class Bullet(Sprite):
    """
    Bullet Sprite\n
    Kills players and enemies on colliding with them\n
    """

    def __init__(
        self,
        shoot_angle_cosine: float,
        shoot_angle_sine: float,
        shoot_point_angle: float,
        owner: Union[Shooter, Enemy],
    ):
        super().__init__(groups[BULLET_GROUP])

        self.owner = owner
        bullet_position = self.calculate_bullet_position(shoot_point_angle)
        self.x = bullet_position[0]
        self.y = bullet_position[1]

        from config.assets import bullet

        self.image: Surface = bullet
        self.rect: Rect = self.image.get_rect(center=(self.x, self.y))

        self.vx = (
            BULLET_VELOCITY
            * shoot_angle_cosine
            * (1 if isinstance(self.owner, Shooter) else -1)
        )
        self.vy = (
            BULLET_VELOCITY
            * shoot_angle_sine
            * (1 if isinstance(self.owner, Shooter) else -1)
        )

    def update(self):
        super().update()
        self.x += self.vx
        self.y += self.vy
        self.rect = self.image.get_rect(center=(self.x, self.y))

        if self.alive and spritecollide(
            self,
            groups[ENEMY_GROUP],
            True,
            (
                lambda sprite1, sprite2: isinstance(sprite1.owner, Shooter)
                and (collide_rect(sprite1, sprite2))
            ),
        ):
            self.owner.score = self.owner.score + 1
            self.kill()

    def calculate_bullet_position(
        self, shoot_point_angle: float
    ) -> Tuple[float, float]:
        if isinstance(self.owner, Shooter):
            return (
                Responsive.center()[0]
                - (Responsive.Player.circle_radius() + Responsive.Player.size())
                * cos(shoot_point_angle),
                Responsive.center()[1]
                - (Responsive.Player.circle_radius() + Responsive.Player.size())
                * sin(shoot_point_angle),
            )
        else:
            return (
                Responsive.center()[0]
                + (Responsive.Enemy.circle_radius() - Responsive.Enemy.size())
                * cos(shoot_point_angle),
                Responsive.center()[1]
                + (Responsive.Enemy.circle_radius() - Responsive.Enemy.size())
                * sin(shoot_point_angle),
            )
