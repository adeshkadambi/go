from __future__ import annotations

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

        liberties = [
            Coordinates(x + 1, y),
            Coordinates(x - 1, y),
            Coordinates(x, y + 1),
            Coordinates(x, y - 1),
        ]

        # filter self.liberties to make sure coordinates cannot be negative
        self.liberties = list(
            filter(lambda coords: coords.x >= 0 and coords.y >= 0, liberties)
        )

        return self.liberties


class StoneGroup:
    """A group of stones on the board."""

    is_black: bool
    stones: list[Stone]
    liberties: list[Coordinates]

    def __init__(self, stone: Stone, groups:list[StoneGroup]):
        self.stones = [stone]
        self.liberties = stone.get_liberties
        self.is_black = stone.is_black
        
        self.update_liberties(groups)

    @property
    def get_liberties(self) -> list[Coordinates]:
        """Returns the liberties of the group."""
        return self.liberties

    @property
    def num_liberties(self) -> int:
        """Returns the number of liberties of the group."""
        return len(self.liberties)

    def add_stone(self, stone: Stone, groups:list[StoneGroup]) -> None:
        """Adds a stone to the group."""
        self.stones.append(stone)
        self.liberties.extend(stone.get_liberties)

        for stone in self.stones:
            if stone.coords in self.liberties:
                self.remove_liberty(stone.coords)
        
        self.update_liberties(groups)

    def add_liberty(self, coords: Coordinates) -> None:
        """Adds a liberty to the group."""
        self.liberties.append(coords)

    def remove_liberty(self, coords: Coordinates) -> None:
        """Removes a liberty from the group."""
        self.liberties.remove(coords)

    def update_liberties(self, groups: list[StoneGroup]) -> None:
        """Updates the liberties of the group by recalculating all liberties."""
        self.liberties = []

        for stone in self.stones:
            self.liberties.extend(stone.get_liberties)

        for stone in self.stones:
            if stone.coords in self.liberties:
                self.remove_liberty(stone.coords)

        for group in groups:
            if group is not self:
                for stone in group.stones:
                    if stone.coords in self.liberties:
                        self.remove_liberty(stone.coords)
        
