import pygame

from config.assets import init_assets
from config.constants import FRAME_RATE, GAME_TITLE
from utils.navigator import Navigator
from utils.responsive import Responsive
from utils.storage import Storage

# Pygame globals
clock: pygame.time.Clock
display_surface: pygame.Surface


def main():
    """
    The entrypoint to the game.
    """
    init_game()
    game_loop()


def init_game():
    """
    Sets up the system and objects.
    """
    global clock, display_surface
    # Set up Pygame
    pygame.init()
    display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    pygame.display.set_caption(GAME_TITLE)

    # Set up globals and assets
    Responsive.init(display_surface.get_size())
    Storage.load()
    init_assets()
    Navigator.init(display_surface)
    Navigator.push("HomeScreen", first=True)


def game_loop():
    """
    The game loop. Updates and draws objects on the current screen at `FRAME_RATE` times per second.
    """
    while True:
        react_to_events()
        Navigator.screen.update()
        Navigator.screen.paint()
        pygame.display.update()
        clock.tick(FRAME_RATE)


def react_to_events():
    """
    Checks and reacts to Pygame events.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Navigator.exit()
        else:
            Navigator.screen.react_to(event)


if __name__ == "__main__":
    main()
