from stones import Stone, StoneGroup
from board import Board


class MoveChecker:
    """Checks if a move is valid and forms connections between groups."""

    def __init__(self):
        pass

    def check_ko(self, board: Board, new_stone: Stone):
        """Checks if the move is a ko."""
        pass

    def check_sd(self, board: Board, new_stone: Stone):
        """Checks if the move is a self-destruct."""
        pass

    def check_on_board(self, board: Board, new_stone: Stone):
        """Checks if the move is on the board."""
        pass

    def is_valid(self, board: Board, new_stone: Stone) -> bool:
        """Checks if the move is valid."""
        return True


class GameController:

    end: bool
    board: Board
    move_checker: MoveChecker

    def __init__(self, size: int = 9):
        self.end = False
        self.board = Board(size)
        self.move_checker = MoveChecker()
    
    @property
    def num_groups(self):
        """Returns the groups on the board."""
        return len(self.board.groups)
    
    @property
    def get_group_stones(self):
        """Returns the stones of each group on the board."""
        return [[group.stones] for group in self.board.groups]

    
    @property
    def get_group_liberties(self):
        """Returns the liberties of each group on the board."""
        return [len(group.get_liberties) for group in self.board.groups]

    def place_stone(self, stone: Stone):
        """Updates the board with a new stone."""
        if self.move_checker.is_valid(self.board, stone):
            self.board.add_stone(stone)
            self.captures()
            self.board.print_board
        else:
            print("Invalid move.")

    def captures(self):
        """Checks if any group is captured."""
        
        # if any group has no liberties, remove it from the board
        for group in self.board.groups:
            if group.num_liberties == 0:
                self.board.groups.remove(group)
                print('capture')
