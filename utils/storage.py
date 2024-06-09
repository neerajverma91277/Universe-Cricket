import json
from os.path import exists
from typing import Dict


class Storage:
    """
    Utility class that handles storage and retrieval of player scores. Uses the file ".data" as dump.
    """

    data: Dict[str, int] = {}

    @classmethod
    def load(cls) -> Dict[str, int]:
        """
        Returns the map in the file ".data".
        """
        cls.data = {}
        if exists(".data"):
            with open(".data", encoding="utf-8") as file:
                cls.data = json.load(file)
        return cls.data

    @classmethod
    def save(cls, name: str, score: int):
        """
        Adds the passed name-score pair to the map in the file ".data".
        :param name: Name of the user.
        :param score: Score of the user.
        """
        cls.data[name] = score
        with open(".data", mode="w", encoding="utf-8") as file:
            json.dump(cls.data, file)
