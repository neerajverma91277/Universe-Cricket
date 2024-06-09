from math import pi
from typing import Optional, Tuple, List

import pygame

from config.constants import DUO_GROUP, ENEMY_COUNT, ENEMY_GROUP
from models.screen import Screen
from .objects import Catcher, dispose_groups, Enemy, groups, init_groups, Shooter
from objects import Background, Button, Text
from utils.navigator import Navigator
from utils.responsive import Responsive


class GameScreen(Screen):
    background: Optional[Background]
    buttons: List[Button]
    display_surface: Optional[pygame.Surface]
    score: Optional[Text]
    ammo: Optional[Text]
    shooter: Optional[Shooter]

    @classmethod
    def init(cls, display_surface: pygame.Surface):
        init_groups()
        cls.display_surface = display_surface
        cls.background = Background(display_surface, rings=True)
        cls.shooter = Shooter()
        Catcher(cls.shooter)
        for i in range(ENEMY_COUNT):
            Enemy((2 * pi * i / ENEMY_COUNT) % (2 * pi), cls.shooter)
        cls.buttons = [
            Button(
                display_surface=display_surface,
                position=(Responsive.width() - 100, 100),
                size=40,
                callback=lambda: Navigator.push("HomeScreen"),
                text="EXIT",
            ),
        ]
        cls.score = Text(
            display_surface=display_surface,
            position=(100, 100),
            size=40,
            const_text="Score",
            text="0",
        )
        cls.ammo = Text(
            display_surface=display_surface,
            position=(100, 150),
            size=50,
            const_text="Ammo",
            text="0",
        )

    @classmethod
    def paint(cls):
        cls.background.draw()
        for group in groups.values():
            group.draw(cls.display_surface)
        for button in cls.buttons:
            button.draw()
        cls.score.draw()
        cls.ammo.draw()
        if not groups[ENEMY_GROUP].sprites():
            Navigator.push("GameOverScreen", score=cls.shooter.score)

    @classmethod
    def update(cls):
        for group in groups.values():
            group.update()
        mouse_position: Tuple[int, int] = pygame.mouse.get_pos()
        for button in cls.buttons:
            button.update(mouse_position)
        try:
            cls.score.update(str(cls.shooter.score))
            cls.ammo.update(str(cls.shooter.ammo))
        except AttributeError:
            pass

    @classmethod
    def react_to(cls, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_LEFT, pygame.K_a]:
                [sprite.move("LEFT") for sprite in groups[DUO_GROUP]]
            elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                [sprite.move("RIGHT") for sprite in groups[DUO_GROUP]]
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit(0)
        elif event.type == pygame.KEYUP:
            [sprite.move("STOP") for sprite in groups[DUO_GROUP]]
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            for button in cls.buttons:
                button.react_to_click()

    @classmethod
    def dispose(cls):
        cls.background = None
        cls.display_surface = None
        dispose_groups()
        cls.buttons = []
