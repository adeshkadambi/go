"""Module for the stones on the board."""


class Coordinates:
    """Coordinates of a stone on the board."""

    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """Returns the coordinates in a string."""
        return f"({self.x}, {self.y})"

    def __eq__(self, other) -> bool:
        """Checks if two coordinates are equal."""
        if isinstance(other, Coordinates):
            return self.x == other.x and self.y == other.y
        return False

    @property
    def get_coords(self) -> tuple:
        """Returns the coordinates of the stone."""
        return (self.x, self.y)


class Stone:
    """A stone on the board."""

    is_black: bool
    location: Coordinates
    liberties: list[Coordinates]

    def __init__(self, x: int, y: int, is_black: bool):
        if x < 0 or y < 0:
            raise ValueError("Stone not on board.")

        self.location = Coordinates(x, y)
        self.liberties = []
        self.is_black = is_black

    def __repr__(self) -> str:
        """Returns the stone in a string."""
        return f"Stone(location:{self.location}, black:{self.is_black})"

    @property
    def coords(self) -> Coordinates:
        """Returns the coordinates of the stone."""
        return self.location

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

    is_black: bool
    stones: list[Stone]
    liberties: list[Coordinates]

    def __init__(self, stone: Stone):
        self.stones = [stone]
        self.liberties = stone.get_liberties
        self.is_black = stone.is_black

    @property
    def get_liberties(self) -> list[Coordinates]:
        """Returns the liberties of the group."""
        return self.liberties

    @property
    def num_liberties(self) -> int:
        """Returns the number of liberties of the group."""
        return len(self.liberties)

    def add_stone(self, stone: Stone) -> None:
        """Adds a stone to the group."""
        self.stones.append(stone)
        self.liberties.extend(stone.get_liberties)

        for stone in self.stones:
            if stone.coords in self.liberties:
                self.liberties.remove(stone.coords)

    def add_liberty(self, coords: Coordinates) -> None:
        """Adds a liberty to the group."""
        self.liberties.append(coords)

    def remove_liberty(self, coords: Coordinates) -> None:
        """Removes a liberty from the group."""
        self.liberties.remove(coords)
