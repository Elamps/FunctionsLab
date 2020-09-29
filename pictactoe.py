game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0], ]

def game_board(player=0, row=0, column=0, just_display=False):
    print("   A  B  C")
    if not just_display:
        game[row][column] = player
    for count, row in enumerate(game):
        print(count, row)
        
game_board(just_display=True)
game_board(current_player, row_choice, col_choice)

# game[2][2] = 1

# game_board()