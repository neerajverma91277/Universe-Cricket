from typing import Callable, Optional, Tuple

import pygame


class Button(pygame.sprite.Sprite):
    """
    A button.

    :param display_surface: The display surface of the game.
    :param position: Center of the button.
    :param text: Text to be displayed.
    :param size: Font size of the text.
    :param callback: Function to be called when button is clicked.
    """

    def __init__(
        self,
        display_surface: pygame.Surface,
        position: Tuple[int, int],
        size: int,
        callback: Optional[Callable],
        text: Optional[str] = None,
        asset: Optional[pygame.Surface] = None,
    ):
        pygame.sprite.Sprite.__init__(self)
        self.display_surface = display_surface
        self.position = position
        self.text = text
        self.size = size
        self.callback = callback
        self.mouse_over = False

        if text is not None:
            self.default_surface: pygame.Surface = create_text_surface(text, size)
            self.highlighted_surface: pygame.Surface = create_text_surface(
                text, int(size * 1.2)
            )
            self.default_rect: pygame.Rect = self.default_surface.get_rect(
                center=position
            )
            self.highlighted_rect: pygame.Rect = self.highlighted_surface.get_rect(
                center=position
            )
        elif asset is not None:
            self.default_surface: pygame.Surface = asset
            self.highlighted_surface: pygame.Surface = pygame.transform.scale(
                asset, (size * 1.2,) * 2
            )
            self.default_rect: pygame.Rect = self.default_surface.get_rect(
                center=position
            )
            self.highlighted_rect: pygame.Rect = self.highlighted_surface.get_rect(
                center=position
            )
        else:
            raise ValueError("`text` and `asset` can't both be `None`")

    def draw(self):
        self.display_surface.blit(self.image, self.rect)

    def update(self, mouse_position: Tuple[int, int]):
        """
        Updates `mouse_over` according to mouse position.
        """
        self.mouse_over = self.rect.collidepoint(mouse_position)
        pass

    def react_to_click(self):
        """
        Calls the `callback` if the mouse click was within button bounds.
        """
        if self.callback is not None and self.mouse_over:
            self.callback()

    @property
    def image(self) -> pygame.Surface:
        return self.highlighted_surface if self.mouse_over else self.default_surface

    @property
    def rect(self) -> pygame.Rect:
        return self.highlighted_rect if self.mouse_over else self.default_rect


def create_text_surface(text: str, size: int) -> pygame.Surface:
    """
    Creates and returns a `Surface` with the passed text printed on it.

    :param text: Text to be printed.
    :param size: Font size of the text.
    """
    font = pygame.font.SysFont("Courier", size, bold=True)
    surface = font.render(text, True, (255, 255, 255))
    return surface.convert_alpha()
