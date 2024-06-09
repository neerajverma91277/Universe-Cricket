from typing import Optional, Any, Callable, List, Tuple

from pygame import Surface, mouse, MOUSEBUTTONUP
from pygame.event import Event

from models.screen import Screen
from objects import Background, Button
from .objects import TextBox
from utils.navigator import Navigator
from utils.responsive import Responsive
from utils.storage import Storage


class GameOverScreen(Screen):
    background: Optional[Background]
    buttons: List[Button]
    textbox: Optional[TextBox]
    save_function: Optional[Callable[[str], None]]

    @classmethod
    def init(cls, display_surface: Surface, **kwargs):
        cls.background = Background(display_surface)
        cls.save_function = lambda name: Storage.save(
            name=name,
            score=kwargs.get("score"),
        )
        cls.textbox = TextBox(
            display_surface,
            position=(Responsive.center()[0], Responsive.center()[1]),
            on_submit=cls.save_function,
            title="NAME",
        )
        cls.buttons = [
            Button(
                display_surface=display_surface,
                position=(Responsive.center()[0], Responsive.center()[1] - 200),
                size=60,
                callback=None,
                text="GAME OVER",
            ),
            Button(
                display_surface=display_surface,
                position=(Responsive.center()[0], Responsive.center()[1] + 100),
                size=60,
                callback=None,
                text=f"SCORE: {kwargs.get('score')}",
            ),
            Button(
                display_surface=display_surface,
                position=(Responsive.center()[0] - 200, Responsive.center()[1] + 250),
                size=40,
                callback=lambda: cls.__save_and_go_to("GameScreen"),
                text="RESTART",
            ),
            Button(
                display_surface=display_surface,
                position=(Responsive.center()[0] + 200, Responsive.center()[1] + 250),
                size=40,
                callback=lambda: cls.__save_and_go_to("HomeScreen"),
                text="HOME",
            ),
        ]

    @classmethod
    def paint(cls):
        cls.background.draw()
        for button in cls.buttons:
            button.draw()
        cls.textbox.draw()

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
        events: Any = [event]
        cls.textbox.update(events)

    @classmethod
    def dispose(cls):
        cls.background = None
        cls.buttons = []

    @classmethod
    def __save_and_go_to(cls, screen_name: str):
        cls.save_function(cls.textbox.value)
        Navigator.push(screen_name)
