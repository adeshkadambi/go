from board import Board
from stones import Stone
from game import GameController

if __name__ == "__main__":
    b1 = Stone(0, 0, is_black=True)
    b2 = Stone(1, 0, is_black=True)

    w1 = Stone(0, 1, is_black=False)
    w2 = Stone(1, 1, is_black=False)
    w3 = Stone(2, 0, is_black=False)

    # x = Board()

    # x.add_stone(b1)
    # x.add_stone(b2)
    # x.add_stone(w1)
    # x.add_stone(w2)
    # x.add_stone(w3)

    # print(x)
    
    # for group in x.groups:
    #     print(group.stones)
    #     print(group.get_liberties)
    #     print(group.num_liberties)

    game = GameController()
    game.place_stone(w1)
    print(game.get_group_stones)
    print(game.get_group_liberties)
    game.place_stone(b1)
    print(game.get_group_stones)
    print(game.get_group_liberties)
    game.place_stone(w2)
    print(game.get_group_stones)
    print(game.get_group_liberties)
    game.place_stone(b2)
    print(game.get_group_stones)
    print(game.get_group_liberties)
    game.place_stone(w3)
    print(game.get_group_stones)
    print(game.get_group_liberties)