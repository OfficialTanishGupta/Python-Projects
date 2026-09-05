def print_board(board):
    """Prints the current state of the game board."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_winner(board, player):
    """Checks if the given player has won the game."""
    win_conditions = [
        [0, 1, 2],
        [3, 4, 5],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def check_draw(board):
    """Checks if the board is completely full, resulting in a draw."""
    return all(space in ["X", "O"] for space in board)


def play_game():
    """Main function to run the Tic-Tac-Toe game loop."""
    board = [str(i) for i in range(1, 10)]
    current_player = "X"
    print("Welcome to Tic-Tac-Toe!")
    print("To make a move, enter the number of the spot you want to take.")

    while True:
        print_board(board)
        try:
            choice = int(
                input(f"Player {current_player}'s turn. Choose a spot (1-9): ")
            )
            position = choice - 1

            if position < 0 or position > 8:
                print("Invalid input! Please choose a number between 1 and 9.")
                continue
            if board[position] in ["X", "O"]:
                print("That spot is already taken! Try another one.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        board[position] = current_player
        if check_winner(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()
