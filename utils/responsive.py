from typing import Callable, Tuple


class Responsive:
    height: Callable[[], int]
    width: Callable[[], int]

    @staticmethod
    def init(size: Tuple[int, int]):
        Responsive.width = lambda: size[0]
        Responsive.height = lambda: size[1]

    @staticmethod
    def center() -> Tuple[int, int]:
        return Responsive.width() // 2, Responsive.height() // 2

    # Player constants
    class Player:
        @staticmethod
        def circle_radius() -> float:
            return 0.168 * Responsive.height()

        @staticmethod
        def size() -> float:
            return 0.0694 * Responsive.height()

        @staticmethod
        def shooting_radius() -> float:
            return 0.347 * Responsive.height()

    # Enemy constants
    class Enemy:
        @staticmethod
        def circle_radius() -> float:
            return 0.397 * Responsive.height()

        @staticmethod
        def size() -> float:
            return 0.0733 * Responsive.height()

    class Bullet:
        @staticmethod
        def size() -> float:
            return 0.0326 * Responsive.height()
