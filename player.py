from stones import Stone

class Player:
    def __init__(self, is_black: bool):
        self.is_black = is_black
    
    def move(self) -> Stone:
        # get user input for a move as a tuple and return it as a Stone
        if self.is_black:
            prompt = "Red - Enter your move (x, y): "
        else:
            prompt = "White - Enter your move (x, y): "

        # get user input for a move as two integers split by comma
        y, x = input(prompt).split(",")

        # return a Stone
        return Stone(int(x), int(y), is_black=self.is_black)
