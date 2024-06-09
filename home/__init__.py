from typing import Optional, List, Tuple

from pygame import mouse, MOUSEBUTTONUP, Surface
from pygame.event import Event

from models.screen import Screen
from utils.navigator import Navigator
from objects import Background, Button
from utils.responsive import Responsive


class HomeScreen(Screen):
    background: Optional[Background]
    buttons: List[Button]

    @classmethod
    def init(cls, display_surface: Surface):
        cls.background = Background(display_surface)
        cls.buttons = [
            Button(
                display_surface=display_surface,
                position=(Responsive.center()[0], Responsive.center()[1] - 100),
                size=80,
                callback=lambda: Navigator.push("GameScreen"),
                text="SPACEBALLS",
            ),
            Button(
                display_surface=display_surface,
                position=(Responsive.center()[0], Responsive.center()[1] + 80),
                size=40,
                callback=lambda: Navigator.push("GameScreen"),
                text="START",
            ),
            Button(
                display_surface=display_surface,
                position=(Responsive.center()[0], Responsive.center()[1] + 150),
                size=40,
                callback=lambda: Navigator.push("HighScoreScreen"),
                text="HIGH SCORES",
            ),
            Button(
                display_surface=display_surface,
                position=(Responsive.center()[0], Responsive.center()[1] + 220),
                size=40,
                callback=lambda: Navigator.exit(),
                text="QUIT",
            ),
        ]

    @classmethod
    def paint(cls):
        cls.background.draw()
        for button in cls.buttons:
            button.draw()

    @classmethod
    def update(cls):
        mouse_position: Tuple[int, int] = mouse.get_pos()
        for button in cls.buttons:
            button.update(mouse_position)

    @classmethod
    def react_to(cls, event: Event):
        if event.type == MOUSEBUTTONUP and event.button == 1:
            for button in cls.buttons:
                button.react_to_click()

    @classmethod
    def dispose(cls):
        cls.background = None
        cls.buttons = []
