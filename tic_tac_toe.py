import random

# Function to print the current board
def print_board(board):
    for i in range(0, 9, 3):
        print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |")
    print()

# Function to check if a player has won
def check_win(board, player):
    win_conditions = [
        [0, 1, 2],  # top row
        [3, 4, 5],  # middle row
        [6, 7, 8],  # bottom row
        [0, 3, 6],  # left column
        [1, 4, 7],  # middle column
        [2, 5, 8],  # right column
        [0, 4, 8],  # diagonal from top-left to bottom-right
        [2, 4, 6],  # diagonal from top-right to bottom-left
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Function to check if there are any empty squares left
def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

# Function to make a move on the board
def make_move(board, position, player):
    if board[position] == ' ':
        board[position] = player
        return True
    return False

# Function for the computer to make a move
def computer_move(board):
    available = available_moves(board)
    return random.choice(available)  # Computer picks a random empty spot

# Function for the human player to make a move
def human_move(board):
    valid_move = False
    while not valid_move:
        try:
            move = int(input("Enter your move (0-8): "))  # Taking input from human player
            if move < 0 or move > 8:
                print("Invalid input. Please choose a number between 0 and 8.")
            elif board[move] != ' ':
                print("This position is already occupied. Choose another position.")
            else:
                valid_move = True
        except ValueError:
            print("Invalid input. Please enter a number.")
    return move

# Function to play the game
def play_game():
    board = [' ' for _ in range(9)]  # Initialize the game board
    current_player = 'X'  # 'X' is the human, 'O' is the computer

    print_board(board)  # Show initial empty board

    while True:
        if current_player == 'X':
            # Human's turn
            move = human_move(board)
            print(f"You chose position {move}")
        else:
            # Computer's turn
            move = computer_move(board)
            print(f"Computer chooses position {move}")

        # Make the move
        make_move(board, move, current_player)
        print_board(board)

        # Check if the current player wins
        if check_win(board, current_player):
            if current_player == 'X':
                print("You win!")
            else:
                print("Computer wins!")
            break

        # Check for tie (board full and no winner)
        if ' ' not in board:
            print("It's a tie!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
if __name__ == "__main__":
    play_game()
