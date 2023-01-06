"""Module for the stones on the board."""


class Coordinates:
    """Coordinates of a stone on the board."""

    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @property
    def get_coords(self) -> tuple:
        """Returns the coordinates of the stone."""
        return (self.x, self.y)


class Stone:
    """A stone on the board."""

    location: Coordinates

    def __init__(self, x: int, y: int):
        self.location = Coordinates(x, y)
        self.liberties = []

    @property
    def coords(self) -> tuple:
        """Returns the coordinates of the stone."""
        return self.location.get_coords

    @property
    def get_liberties(self) -> list[Coordinates]:
        """Returns the liberties of the stone."""
        x, y = self.location.get_coords
        self.liberties = [
            Coordinates(x + 1, y),
            Coordinates(x - 1, y),
            Coordinates(x, y + 1),
            Coordinates(x, y - 1),
        ]
        return self.liberties


class StoneGroup:
    """A group of stones on the board."""

    stones: list[Stone]
    liberties: list[Coordinates]

    def __init__(self, stone: Stone):
        self.stones = [stone]
        self.liberties = stone.get_liberties

    @property
    def get_liberties(self) -> list[Coordinates]:
        """Returns the liberties of the group."""
        return self.liberties

    def add_stone(self, stone: Stone) -> None:
        """Adds a stone to the group."""
        self.stones.append(stone)
        self.liberties.extend(stone.get_liberties)

        for stone in self.stones:
            if stone.coords in self.liberties:
                self.liberties.remove(stone.coords)

    # def connected(group: StoneGroup, other_groups: list[StoneGroup]) -> bool:
    #     """Checks if another group is in the liberties (i.e. connected) of the group."""
    #     for group in other_groups:
    #         for stone in group.stones:
    #             if stone.coords in self.liberties:
    #                 return True
