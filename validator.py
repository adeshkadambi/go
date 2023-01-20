from copy import deepcopy
from board import Board
from stones import Stone

class MoveChecker:
    """Checks if a move is valid and forms connections between groups."""

    def ko(self, board: Board, new_stone: Stone) -> bool:
        """Checks if the move is a ko."""

        # check if board has at least 2 states
        if len(board.board_states) < 2:
            return False

        # copy of entire board
        board_copy = deepcopy(board)

        # previous board state
        previous_board = board.board_states[-2]

        # check if the previous board state is the same as the current board state if stone is added
        board_copy.add_stone(new_stone)

        return board_copy.board == previous_board

    def sd(self, board: Board, new_stone: Stone):
        """Checks if the move is a self-destruct."""
        pass

    def on_board(self, board: Board, new_stone: Stone) -> bool:
        """Checks if the move is on the board."""
        return 0 <= new_stone.coords.x < board.size and 0 <= new_stone.coords.y < board.size
    
    def stone_exists(self, board: Board, new_stone: Stone) -> bool:
        """Checks if a stone already exists at new_stone's coords."""
        return board.board[new_stone.coords.x][new_stone.coords.y] is not None

    def is_valid(self, board: Board, new_stone: Stone) -> bool:
        """Checks if the move is valid."""
        
        # check if the move is on the board
        if not self.on_board(board, new_stone):
            print("Move is not on the board.")
            return False
        
        # check if the move is a ko
        if self.ko(board, new_stone):
            print("Ko.")
            return False
        
        # check if a stone already exists at the coords
        if self.stone_exists(board, new_stone):
            print("Stone already exists at these coords.")
            return False
        
        # check if the move is a self-destruct
        if self.sd(board, new_stone):
            pass # todo

        return True