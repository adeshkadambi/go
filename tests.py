from board import Board
from stones import Stone
from game import GameController

if __name__ == "__main__":
    b1 = Stone(0, 0, is_black=True)
    b2 = Stone(1, 0, is_black=True)

    w1 = Stone(0, 1, is_black=False)
    w2 = Stone(1, 1, is_black=False)
    w3 = Stone(2, 0, is_black=False)

    moves = [w1, b1, w2, b2, w3]

    game = GameController(size=5)
    game.start_game()

    # for move in moves:
    #     game.place_stone(move)
    #     print(game.get_group_stones)
    #     print(game.get_group_liberties)
    #     print('\n')