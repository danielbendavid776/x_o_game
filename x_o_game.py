
def init_board():
    return [ [" ", " ", " "], [" ", " ", " "],    [" ", " ", " "], ]

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def get_move(board, mark):
    while True:
        square = int(input(f"chose a square between 1 - 9,{mark} player: "))

        if square < 1 or square > 9:
            print("invalid input")
            continue

        row = (square - 1) // 3
        col = (square - 1) % 3

        if board[row][col] != " ":
            print("the square is occupied")
            continue

        return row, col

def check_winner(board, mark):
    for row in board:
        if row[0] == mark and row[1] == mark and row[2] == mark:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == mark:
            return True
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True

    return False

def is_board_full(board):
    for row in board:
        for col in row:
            if col == " ":
                return False
    return True

def ask_play_again():
    while True:
        answer = input("Do you want to play again? (y/n): ")
        if answer.lower() == "y":
            return True
        elif answer.lower() == "n":
            return False
        else:
            print("invalid input")


def play_game():
    board = init_board()
    print_board(board)


    while True:
        row, col = get_move(board, 'X')
        board[row][col] = "X"
        print_board(board)

        if check_winner(board, "X"):
            print('player X win')
            return 'X'
        if is_board_full(board):
            print('draw')
            return 'draw'

        row, col = get_move(board, 'O')
        board[row][col] = "O"
        print_board(board)

        if check_winner(board, "O"):
            print('player O win')
            return 'O'
        if is_board_full(board):
            print('draw')
            return 'draw'

x_counter = 0
o_counter = 0

while True:
    result = play_game()
    if result == 'X':
        x_counter += 1
    elif result == 'O':
        o_counter += 1
    print(f'player X wins: {x_counter} | player O wins: {o_counter}')

    if not ask_play_again():
        print('thank you for playing')
        break

