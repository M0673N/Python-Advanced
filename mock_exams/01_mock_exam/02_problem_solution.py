player_1, player_2 = input().split(", ")
dart_board = []
for i in range(7):
    dart_board.append([i for i in input().split()])

counter = 0
player_1_turns = 0
player_1_score = 501
player_2_turns = 0
player_2_score = 501
while True:
    coordinates = input().split(", ")
    row = int(coordinates[0][1:])
    col = int(coordinates[1][:-1])

    if counter % 2 == 0:
        if not 0 <= row < 7 or not 0 <= col < 7:
            player_1_turns += 1
        elif dart_board[row][col].isdigit():
            player_1_turns += 1
            player_1_score -= int(dart_board[row][col])
        elif dart_board[row][col] == "D":
            player_1_turns += 1
            player_1_score -= (int(dart_board[row][0]) + int(dart_board[row][len(dart_board) - 1]) + int(
                dart_board[0][col]) + int(dart_board[len(dart_board) - 1][col])) * 2
        elif dart_board[row][col] == "T":
            player_1_turns += 1
            player_1_score -= (int(dart_board[row][0]) + int(dart_board[row][len(dart_board) - 1]) + int(
                dart_board[0][col]) + int(dart_board[len(dart_board) - 1][col])) * 3
        elif dart_board[row][col] == "B":
            player_1_turns += 1
            print(f"{player_1} won the game with {player_1_turns} throws!")
            break
    else:
        if not 0 <= row < 7 or not 0 <= col < 7:
            player_2_turns += 1
        elif dart_board[row][col].isdigit():
            player_2_turns += 1
            player_2_score -= int(dart_board[row][col])
        elif dart_board[row][col] == "D":
            player_2_turns += 1
            player_2_score -= (int(dart_board[row][0]) + int(dart_board[row][len(dart_board) - 1]) + int(
                dart_board[0][col]) + int(dart_board[len(dart_board) - 1][col])) * 2
        elif dart_board[row][col] == "T":
            player_2_turns += 1
            player_2_score -= (int(dart_board[row][0]) + int(dart_board[row][len(dart_board) - 1]) + int(
                dart_board[0][col]) + int(dart_board[len(dart_board) - 1][col])) * 3
        elif dart_board[row][col] == "B":
            player_2_turns += 1
            print(f"{player_2} won the game with {player_2_turns} throws!")
            break

    counter += 1

    if player_1_score <= 0:
        print(f"{player_1} won the game with {player_1_turns} throws!")
        break
    elif player_2_score <= 0:
        print(f"{player_2} won the game with {player_2_turns} throws!")
        break
