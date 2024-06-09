from abc import ABC, abstractmethod

import pygame


class Screen(ABC):
    """
    Abstract base class for all the screens in the game. Enforces structure and type safety.

    All methods and variables will be static.
    """

    @classmethod
    @abstractmethod
    def init(cls, display_surface: pygame.Surface):
        """
        Initializer. Loads one-time data into the static variables.
        """

    @classmethod
    @abstractmethod
    def paint(cls):
        """
        Painter. Paints one frame of the screen.
        """

    @classmethod
    @abstractmethod
    def update(cls):
        """
        Updater. Updates screen state between frames.
        """

    @classmethod
    @abstractmethod
    def react_to(cls, event: pygame.event.Event):
        """
        Listener. Checks for events and reacts appropriately.
        """

    @classmethod
    @abstractmethod
    def dispose(cls):
        """
        Disposer. Destroys memory-heavy objects when screen is removed.
        """
