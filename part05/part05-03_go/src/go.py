# Write your solution here
def who_won(game_board: list):
    pieces_one = 0
    pieces_two = 0
    for i in game_board:
        pieces_one += i.count(1)
        pieces_two += i.count(2)
    if pieces_one > pieces_two :
        return 1
    elif pieces_two > pieces_one:
        return 2
    else:
        return 0