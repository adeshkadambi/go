from copy import deepcopy

from stones import Stone
from board import Board
from player import Player


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
        board_copy.consolidate_captures()

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


class GameController:

    end: bool
    board: Board
    total_moves: int
    move_checker: MoveChecker

    def __init__(self, size: int = 9):
        self.end = False
        self.total_moves = 0
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
        return [[group.get_liberties] for group in self.board.groups]
    
    @property
    def is_game_over(self):
        """Returns True if the game is over."""
        return self.end

    def start_game(self) -> None:
        """Starts the game."""
        self.board.print_board()
        p1 = Player(True)
        p2 = Player(False)

        while not self.end:
            # alternate moves between p1 and p2 until game ends
            self.player_turn(p1, self.move_checker)
            self.player_turn(p2, self.move_checker)

            if self.total_moves == 10:
                self.end = True
                print("Game over.")

    def place_stone(self, stone: Stone):
        """Updates the board with a new stone."""
        if self.move_checker.is_valid(self.board, stone):
            self.board.add_stone(stone)
            self.board.consolidate_captures()
            self.board.append_board_state()
            self.board.print_board()
        else:
            print("Invalid move.")

    def player_turn(self, player: Player, checker:MoveChecker) -> None:
        """Player takes a turn."""
        
        # get player's move
        move = player.move()

        # check if move is valid else get new move
        while not checker.is_valid(self.board, move):
            move = player.move()
        
        # place stone
        self.place_stone(move)

        # increment total moves
        self.total_moves += 1