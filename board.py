from stones import Stone, StoneGroup
from colored import fg, attr # type: ignore


class Board:
    """Board model and visualisation."""

    size: int
    board: list[list[Stone | None]]
    board_states: list[list[list[Stone | None]]]
    groups: list[StoneGroup]

    def __init__(self, size: int = 9):
        self.size = size
        self.groups = []
        self.board_states = []
        self.board = [[None for _ in range(size)] for _ in range(size)]

    def __str__(self):
        """Visualize the board, printing black stones as red text and white stones as white text."""
        board = ""
        for row in self.board:
            for stone in row:
                if stone is None:
                    board += f" {fg(0)}.{attr(0)} "
                elif stone.is_black:
                    board += f" {fg(1)}O{attr(0)} "
                else:
                    board += f" {fg(15)}O{attr(0)} "
            board += "\n"
        return board

    def print_board(self) -> None:
        """Prints the board."""
        print(self)

    def append_board_state(self) -> None:
        """Appends the current board state to the board_states list."""
        self.board_states.append(self.board)

    @staticmethod
    def form_connection(stone: Stone, group: StoneGroup, all_groups: list[StoneGroup]) -> None:
        """Forms a connection between stone and group."""
        if stone.is_black == group.is_black:
            group.add_stone(stone, all_groups)
        else:
            group.remove_liberty(stone.coords)

    def add_stone(self, stone: Stone) -> None:
        """Add a stone to the board."""
        self.board[stone.coords.x][stone.coords.y] = stone
        self.connected_to_group(stone, self.groups)
        self.consolidate_captures()

    def connected_to_group(self, new_stone: Stone, groups: list[StoneGroup]) -> None:
        """Checks if a stone is connected to another group and forms connections."""

        if len(groups) == 0:
            groups.append(StoneGroup(new_stone, groups))

        for group in groups:
            if new_stone.coords in group.get_liberties:
                self.form_connection(new_stone, group, groups)

        # if new stone isn't in a group, make a new group
        if new_stone not in [stone for group in groups for stone in group.stones]:
            groups.append(StoneGroup(new_stone, groups))

    def consolidate_captures(self):
        """Checks if any group is captured."""
        
        # if any group has no liberties, remove it from the board
        for group in self.groups:
            if group.num_liberties == 0:
                # remove the group from the board and set the stones to empty
                for stone in group.stones:
                    self.board[stone.coords.x][stone.coords.y] = None

                self.groups.remove(group)
        
        # update all groups' liberties
        for group in self.groups:
            group.update_liberties(self.groups)

