"""Scratch file for testing code"""
import stones
import game

if __name__ == "__main__":
    b1 = stones.Stone(0, 0, True)
    g1 = stones.StoneGroup(b1)
    b2 = stones.Stone(1, 0, True)
    w1 = stones.Stone(0, 1, False)

    print(g1.stones, "\n", g1.get_liberties, "\n")

    game.form_connection(b2, g1)

    print(g1.stones, "\n", g1.get_liberties)
    
    game.form_connection(w1, g1)

    print(g1.stones, "\n", g1.get_liberties)
    