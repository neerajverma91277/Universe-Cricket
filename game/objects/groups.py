from typing import Dict
from pygame.sprite import Group

from config.constants import BULLET_GROUP, DUO_GROUP, ENEMY_GROUP

groups: Dict[str, Group] = {}


def init_groups():
    """
    initialises all the sprite groups in the game
    """
    global groups
    groups[ENEMY_GROUP] = Group()
    groups[BULLET_GROUP] = Group()
    groups[DUO_GROUP] = Group()


def dispose_groups():
    """
    Destroys all the sprite groups in the game.
    """
    global groups
    for grp in groups:
        groups[grp].empty()
