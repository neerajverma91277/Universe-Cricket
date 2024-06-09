from math import cos, sin, pi
from typing import Literal, Tuple, List

from pygame import Surface, time
from pygame.sprite import Sprite, spritecollide, collide_circle, collide_rect
from pygame.transform import rotate

from config.constants import (
    BULLET_GROUP,
    DUO_GROUP,
    ENEMY_GROUP,
    INITIAL_AMMO,
    PLAYER_SPEED,
    SHOOTING_FREQUENCY,
)
from utils.navigator import Navigator

from .groups import groups
from utils.responsive import Responsive


class Duo(Sprite):
    """
    Parent object for the two protagonists of the game, the shooter and the catcher.

    Not Intended to be instantiated
    """

    def __init__(self):
        from config.assets import shooter

        Sprite.__init__(self, groups[DUO_GROUP])

        self.angle: float = 0
        self.direction: int = 0
        self.ammo = INITIAL_AMMO
        self.score = 0
        self.clean_image = Surface(size=self.calculate_position())
        self.rect = shooter.get_rect(center=(self.calculate_position()))

    def update(self):
        super().update()
        self.angle += self.direction * PLAYER_SPEED
        self.rect = self.image.get_rect(center=self.calculate_position())

    def move(self, direction: Literal["LEFT", "RIGHT", "STOP"]):
        if direction == "LEFT":
            self.direction = -1
        elif direction == "RIGHT":
            self.direction = 1
        elif direction == "STOP":
            self.direction = 0

    def calculate_position(self) -> Tuple[float, float]:
        """
        calculates x y coordinate of Duo
        """
        return 0, 0


class Shooter(Duo):
    """
    Shooter sprite
    """

    def __init__(self):
        super().__init__()

        from config.assets import shooter

        self.radius = Responsive.Player.shooting_radius()
        self.clean_image = shooter
        self.image = rotate(self.clean_image, (pi - self.angle) * (180 / pi))
        self.should_shoot = True
        self.last_shoot = time.get_ticks()

    def update(self):
        super().update()
        self.image = rotate(self.clean_image, (pi - self.angle) * (180 / pi))
        if self.alive and spritecollide(
            self,
            groups[BULLET_GROUP],
            True,
            (
                lambda sprite1, sprite2: (not isinstance(sprite2.owner, Shooter))
                and (collide_rect(sprite1, sprite2))
            ),
        ):
            Navigator.push("GameOverScreen", score=self.score)
            return

        if self.alive and spritecollide(
            self, groups[ENEMY_GROUP], False, collide_circle
        ):
            enemy_List: List = spritecollide(
                self, groups[ENEMY_GROUP], False, collide_circle
            )
            if self.should_shoot and self.ammo > 0:
                self.shoot(enemy_List)
                self.last_shoot = time.get_ticks()
                self.should_shoot = False

        if (
            not self.should_shoot
        ) and time.get_ticks() - self.last_shoot >= SHOOTING_FREQUENCY:
            self.should_shoot = True

    def shoot(self, enemies: List):
        from .bullet import Bullet

        for enemy in enemies:
            # Enemy rect center
            enemy_position = enemy.calculate_position()
            x = enemy_position[0]
            y = enemy_position[1]

            # Player rect center
            self_position = self.calculate_position()
            a = self_position[0]
            b = self_position[1]

            diag = ((x - a) ** 2 + (y - b) ** 2) ** 0.5
            shoot_angle_cosine = (x - a) / diag
            shoot_angle_sine = (y - b) / diag
            self.ammo = self.ammo - 1
            Bullet(shoot_angle_cosine, shoot_angle_sine, self.angle, self)

    def calculate_position(self) -> Tuple[float, float]:
        super().calculate_position()
        return (
            Responsive.center()[0]
            - Responsive.Player.circle_radius() * cos(self.angle),
            Responsive.center()[1]
            - Responsive.Player.circle_radius() * sin(self.angle),
        )


class Catcher(Duo):
    """
    Catcher Sprite
    """

    def __init__(self, shooter: Shooter):
        super().__init__()

        from config.assets import catcher

        self.clean_image = catcher
        self.image = rotate(self.clean_image, (pi - self.angle) * (180 / pi))
        self.shooter = shooter

    def update(self):
        super().update()
        self.image = rotate(self.clean_image, (pi - self.angle) * (180 / pi))
        if self.alive and spritecollide(
            self,
            groups[BULLET_GROUP],
            True,
            (
                lambda sprite1, sprite2: (not isinstance(sprite2.owner, Shooter))
                and (collide_rect(sprite1, sprite2))
            ),
        ):
            self.shooter.ammo = self.shooter.ammo + 1
            self.shooter.score = self.shooter.score + 1
            pass

    def calculate_position(self) -> Tuple[float, float]:
        super().calculate_position()
        return (
            Responsive.center()[0]
            + Responsive.Player.circle_radius() * cos(self.angle),
            Responsive.center()[1]
            + Responsive.Player.circle_radius() * sin(self.angle),
        )
