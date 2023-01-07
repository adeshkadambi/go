from stones import Stone, StoneGroup

def 

def form_connection(stone: Stone, group: StoneGroup) -> None:
    """Forms a connection between stone and group."""
    if stone.black == group.black:
        group.add_stone(stone)
    else:
        group.remove_liberty(stone.coords)


def connected_to_group(new_stone: Stone, groups: list[StoneGroup]) -> bool:
    """Checks if a stone is connected to another group."""

    for group in groups:
        if new_stone.coords in group.get_liberties:
            form_connection(new_stone, group)
            return True
    

    return False
