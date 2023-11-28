# tictactoe.py

def print_board(board):
    print("---------")
    for row in board:
        print("| " + " ".join(row) + " |")
    print("---------")

def read_input():
    cells_input = input("Enter cells: ")
    if len(cells_input) != 9:
        print("Enter a string with exactly 9 characters.")
        return None
    board = [[cells_input[i] for i in range(j, j + 3)] for j in range(0, 9, 3)]
    return board

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '_':
            return f"{board[i][0]} wins"
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '_':
            return f"{board[0][i]} wins"
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_':
        return f"{board[0][0]} wins"
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_':
        return f"{board[0][2]} wins"
    return None

def analyze_game_state(board):
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)
    if abs(x_count - o_count) >= 2:
        return "Impossible"
    winner = check_winner(board)
    if winner:
        return winner
    if any('_' in row for row in board):
        return "Game not finished"
    else:
        return "Draw"

def make_move(board, player):
    while True:
        try:
            coordinates = input("Enter the coordinates: ")
            x, y = map(int, coordinates.split())
            if 1 <= x <= 3 and 1 <= y <= 3:
                if board[x - 1][y - 1] == '_':
                    board[x - 1][y - 1] = player
                    break
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        except ValueError:
            print("You should enter numbers!")

def main():
    board = [["_" for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)
        make_move(board, 'X')
        result = analyze_game_state(board)
        if result != "Game not finished":
            print_board(board)
            print(result)
            break

        print_board(board)
        make_move(board, 'O')
        result = analyze_game_state(board)
        if result != "Game not finished":
            print_board(board)
            print(result)
            break

if __name__ == "__main__":
    main()
