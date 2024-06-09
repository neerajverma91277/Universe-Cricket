from typing import Type

import pygame

from models.screen import Screen


class Navigator:
    """
    Utility class to store current screen and call appropriate handlers when screen change is requested.
    """

    display_surface: pygame.Surface
    screen: Type[Screen]

    @staticmethod
    def init(display_surface: pygame.Surface):
        """
        Initializes the class variables.

        :param display_surface: The base surface on which all the other surfaces are `blit`.
        """
        Navigator.display_surface = display_surface

    @staticmethod
    def push(screen_name: str, first: bool = False, **kwargs):
        """
        Replaces current screen with passed screen. Calls appropriate handlers.

        :param screen_name: The new screen to push.
        :param first: Whether this is the first screen to be pushed.
        """
        if not first:
            # Call disposer of old screen
            Navigator.screen.dispose()
        # Update screen
        from game import GameScreen
        from over import GameOverScreen
        from score import HighScoreScreen
        from home import HomeScreen

        if screen_name == "GameScreen":
            Navigator.screen = GameScreen
        elif screen_name == "GameOverScreen":
            Navigator.screen = GameOverScreen
        elif screen_name == "HighScoreScreen":
            Navigator.screen = HighScoreScreen
        elif screen_name == "HomeScreen":
            Navigator.screen = HomeScreen
        # Call initializer of new screen
        Navigator.screen.init(Navigator.display_surface, **kwargs)

    @staticmethod
    def exit():
        Navigator.screen.dispose()
        pygame.quit()
        exit()
