from stones import Stone
from board import Board
from player import Player
from validator import MoveChecker


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