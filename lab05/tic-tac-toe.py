# Joseph Naze - CIS109 - TIC-TAC-TOE game

import itertools

def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != '-':
            return True
        else:
            return False
        
    for row in matrix:
        print(row)
        if all_same(row):
            print(f" \nPlayer {row[0]} is the winner!\n \nGame Over!\nThanks for Playing!\n")
            return True

    diags = []
    for col, row in enumerate(reversed(range(len(matrix)))):
        diags.append(matrix[row][col])
    if all_same(diags):
         print(f" \nPlayer {diags[0]} is the winner!\n \nGame Over!\nThanks for Playing!\n")
         return True
    
    diags = []
    for ix in range(len(matrix)):
        diags.append(matrix[ix][ix])
    if all_same(diags):
        print(f" \nPlayer {diags[0]} is the winner!\n \nGame Over!\nThanks for Playing!\n")
        return True
    

    for col in range(len(matrix)):
        check = []

        for row in matrix:
            check.append(row[col])

        if all_same(check):
            print(f" \nPlayer {check[0]} is the winner!\n \nGame Over!\nThanks for Playing!\n")
            return True

    return False

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != "-":
            print("Sorry, seat's taken! Choose another spot!")
            return game_map, False
        print("    0    1    2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(matrix):
            print(count, row)
        return game_map, True

    except IndexError as e:
        print("Error: Make sure you input row/column as 0, 1, or 2.", e)
        return game_map,  False

    except Exception as e:
        print("Something went very wrong!", e)
        return game_map, False

play = True
players = ["X", "O"]
while play:
    print("TIC - TAC - TOE")
    matrix = [["-", "-", "-"], 
              ["-", "-", "-"], 
              ["-", "-", "-"]]

    game_won = False
    matrix, _ = game_board(matrix, just_display=True)
    player_choice = itertools.cycle(["X", "O"])
    while not game_won:
        current_player = next(player_choice)
        print(f" \n{current_player}'s Turn\n")
        played = False

        while not played:
            row_choice = int(input("Enter row (0-2): "))
            column_choice = int(input("Enter column (0-2): "))
            matrix, played = game_board(matrix, current_player, row_choice, column_choice)

        if win(matrix):
            game_won = True
            again = input("The game has ended. Would you like to play again? type y or n: ")
            if again.lower() == "y":
                print(" \nRestarting")
            elif again.lower() == "n":
                print(" \nGoodbye!")
                play = False
            else:
                print(" \nNot a valid input, Goodbye!")
                play = False


