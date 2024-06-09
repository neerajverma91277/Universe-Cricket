from typing import Callable, Tuple

import pygame
from pygame import Surface, KEYDOWN
from pygame.event import Event
from pygame.font import SysFont
from pygame_textinput import TextInputVisualizer


class TextBox(TextInputVisualizer):
    """
    Wrapper for `TextInputVisualizer`. Extends the class with dynamic positioning, a prefix and submitting capabilities.
    """

    def __init__(
        self,
        display_surface: Surface,
        position: Tuple[int, int],
        on_submit: Callable,
        title: str,
    ):
        TextInputVisualizer.__init__(
            self,
            antialias=True,
            font_object=SysFont("Courier", 40, bold=True),
            font_color=(255, 255, 255),
            cursor_color=(255, 255, 255),
        )
        # Drawing
        self.display_surface = display_surface
        self.position = position
        self.rect = self.surface.get_rect(center=position)
        # Submitting
        self.submitted = False
        self.on_submit = on_submit
        # Prefixing
        self.value = f"{title}: "
        self.manager.cursor_pos = len(title) + 2

    def draw(self):
        self.display_surface.blit(self.surface, self.rect)

    def update(self, events: Event):
        # Input
        if not self.submitted:
            TextInputVisualizer.update(self, events)
            if events[0].type == KEYDOWN and events[0].key == pygame.K_RETURN:
                self.on_submit(self.value)
                self.submitted = True
                self.cursor_blink_interval = 100000
                # ^ Makes it seem like the blinking has stopped.
                self.cursor_visible = False
        # Reposition
        self.rect = self.surface.get_rect(center=self.position)
