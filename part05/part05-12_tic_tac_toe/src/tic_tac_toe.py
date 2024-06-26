# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if x > 2 or x < 0:
        return False
    if y > 2 or y < 0:
        return False

    if game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    return False

