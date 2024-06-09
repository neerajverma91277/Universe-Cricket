from typing import Optional

from pygame import Surface, mouse, MOUSEBUTTONUP
from pygame.event import Event

from models.screen import Screen
from objects import Background, Button
from utils.navigator import Navigator
from utils.responsive import Responsive
from utils.storage import Storage


class HighScoreScreen(Screen):
    background: Optional[Background]
    buttons: "list[Button]"

    @classmethod
    def init(cls, display_surface: Surface):
        cls.background = Background(display_surface)
        scores = {
            k[6:]: v
            for k, v in sorted(Storage.data.items(), key=lambda item: -item[1])[:3]
        }
        if len(scores) == 0:
            scores[""] = ""
            scores["No highscores yet"] = ""
        cls.buttons = [
            Button(
                display_surface=display_surface,
                position=(Responsive.center()[0], Responsive.center()[1] - 200),
                size=60,
                callback=None,
                text="HIGH SCORES",
            ),
            Button(
                display_surface=display_surface,
                position=(Responsive.center()[0], Responsive.center()[1] + 250),
                size=40,
                callback=lambda: Navigator.push("HomeScreen"),
                text="HOME",
            ),
        ] + [
            Button(
                display_surface=display_surface,
                position=(
                    Responsive.center()[0],
                    Responsive.center()[1] - 70 + 70 * (i + 1),
                ),
                size=40,
                callback=None,
                text=f"{score[0]} {score[1]}",
            )
            for i, score in enumerate(scores.items())
        ]

    @classmethod
    def paint(cls):
        cls.background.draw()
        for button in cls.buttons:
            button.draw()

    @classmethod
    def update(cls):
        mouse_position: tuple[int, int] = mouse.get_pos()
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
