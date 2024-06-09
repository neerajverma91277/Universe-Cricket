from typing import Tuple
from pygame import Rect, sprite, font, Surface


class Text(sprite.Sprite):
    """
    Text object

    class used to draw and update any text in the game
    """

    def __init__(
        self,
        text: str,
        const_text: str,
        position: Tuple[float, float],
        size: float,
        display_surface: Surface,
    ) -> None:
        self.text = text
        self.const_text = const_text
        self.size = size
        self.position = position
        self.text_surface = self.font_surface()
        self.rect = self.text_surface.get_rect(center=self.position)
        self.display_surface = display_surface

    def draw(self) -> None:
        """
        draws text on the `display_surface`
        """
        self.display_surface.blit(self.text_surface, self.rect)

    def update(self, text: str) -> None:
        """
        updates text with new `text` value
        """
        super().update()
        self.text = text
        self.text_surface = self.font_surface()
        self.rect = self.text_surface.get_rect(center=self.position)

    def font_surface(self) -> Surface:
        """
        creates a rect with rendered `text` and at provided `position`
        """
        text_font = font.SysFont("Courier", self.size, bold=True)
        surface = text_font.render(
            f"{self.const_text} {self.text}", True, (255, 255, 255)
        )
        return surface.convert_alpha()
