from pygame import Surface
from pygame.sprite import Sprite
from pygame.transform import scale

from utils.responsive import Responsive


class Background(Sprite):
    """
    The background.

    Intended to be instantiated only once.

    :param display_surface: The display surface of the game.
    :param rings: Whether to display the duo and enemy rings.
    """

    def __init__(self, display_surface: Surface, rings: bool = False):
        from config.assets import (
            background,
            duo_circle,
            enemy_circle,
            earth,
            planet0,
            spacecraft0,
            spaceship,
            planet1,
            planet2,
            gradient,
            rock0,
            rock1,
        )

        Sprite.__init__(self)
        self.display_surface = display_surface
        self.background = scale(background, (Responsive.width(), Responsive.height()))
        self.duo_circle = duo_circle if rings else None
        self.enemy_circle = enemy_circle if rings else None
        self.earth = earth
        self.planet0 = planet0
        self.spacecraft0 = spacecraft0
        self.spaceship = spaceship
        self.planet1 = planet1
        self.planet2 = planet2
        self.gradient = gradient
        self.rock0 = rock0
        self.rock1 = rock1

    def draw(self):
        self.display_surface.blit(self.background, (0, 0))
        if self.duo_circle is not None:
            self.display_surface.blit(
                self.earth, self.earth.get_rect(center=Responsive.center())
            )
            self.display_surface.blit(
                self.planet0, self.planet0.get_rect(topright=(Responsive.width(), 0))
            )
            self.display_surface.blit(
                self.spacecraft0,
                self.spacecraft0.get_rect(
                    center=(
                        Responsive.width() / 2 + Responsive.Enemy.circle_radius() + 10,
                        (Responsive.Player.circle_radius() + 50),
                    )
                ),
            )
            self.display_surface.blit(
                self.spaceship,
                self.spaceship.get_rect(
                    center=(
                        Responsive.width() / 2 - Responsive.Enemy.circle_radius() - 200,
                        (Responsive.Player.circle_radius() + 50),
                    )
                ),
            )
            self.display_surface.blit(
                self.planet1,
                self.planet1.get_rect(
                    center=(
                        2 * Responsive.Player.circle_radius(),
                        Responsive.height() - Responsive.Player.circle_radius(),
                    )
                ),
            )
            self.display_surface.blit(
                self.planet2,
                self.planet2.get_rect(
                    bottomleft=(
                        0,
                        Responsive.height(),
                    )
                ),
            )
            self.display_surface.blit(
                self.gradient,
                self.gradient.get_rect(
                    center=(
                        Responsive.width() / 2 + Responsive.Player.circle_radius(),
                        Responsive.height() / 2 + Responsive.Player.circle_radius(),
                    )
                ),
            )
            self.display_surface.blit(
                self.rock0,
                self.rock0.get_rect(
                    center=(
                        Responsive.width() / 2 + Responsive.Enemy.circle_radius(),
                        Responsive.height() / 2 + Responsive.Enemy.circle_radius(),
                    )
                ),
            ),
            self.display_surface.blit(
                self.rock1,
                self.rock1.get_rect(
                    bottomright=(
                        Responsive.width(),
                        Responsive.height(),
                    )
                ),
            )
            self.display_surface.blit(
                self.duo_circle,
                self.duo_circle.get_rect(
                    center=Responsive.center(),
                ),
            )
            self.display_surface.blit(
                self.enemy_circle,
                self.enemy_circle.get_rect(
                    center=Responsive.center(),
                ),
            )
