# py-go
Implementation of the go board game in Python.

```mermaid
---
title: Class Diagram
---
classDiagram

    GameController <-- BoardModel
    BoardModel <-- StoneGroup
    StoneGroup <-- Stone
    GameController <-- MoveChecker
    GameController <-- PlayerView
    Stone <-- Coordinates
    StoneGroup <-- Coordinates

    class BoardModel {
        board:[[*StoneGroup]]
        groups_white:[Stone]
        groups_black:[Stone]
    }

    class GameController {
        - end: bool
        - checker: MoveChecker
        - board: BoardModel
        - turns: [Stone]

        place_stone(Stone, checker) -> None
        update_board(Stone)
    }

    class MoveChecker{
        - check_ko()
        - check_sd()
        + check_move(Stone, turns) -> Bool
    }

    class PlayerView {
        color: bool

        + print_board(BoardModel)
    }

    class Stone {
        location:Coordinates
    }

    class Coordinates {
        x:int
        y:int
        get_coords() -> (int, int)
    }

    class StoneGroup {
        stones:[Stone]
        liberties:[Coordinates]

        remove_liberty(Stone) ->
        delete   
    }
```

- TODO check which group liberty was played
- Game End: (1) if player resigns (2) two passes in a row (3) no intersections left

## Flow:
- GameController.place_stone(Coordinates)
- if MoveChecker.check_move():
    - check stone group and create one if none
    - calculate liberties and delete groups if 0
    - update board
    - update view