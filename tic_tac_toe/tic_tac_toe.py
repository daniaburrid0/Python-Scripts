from rich.console import Console
import random

console = Console()

# Initialize the board and players
def initialize_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human = "X"
    computer = "O"
    return board, human, computer

# Function to display the board using Rich
def display_board(board):
    console.print("Current board:")
    for row in board:
        console.print(" | ".join(row))
        console.print("-" * 9)

# Function to get human player's move
def get_human_move(board, player):
    valid_move = False
    while not valid_move:
        move = input(f"Enter your move for {player} (row col): ").split()
        if len(move) != 2:
            console.print("Invalid input. Please enter row and column separated by space.")
            continue
        row, col = map(int, move)
        if row < 0 or row > 2 or col < 0 or col > 2:
            console.print("Invalid move. Please enter a valid row and column between 0 and 2.")
            continue
        if board[row][col] != " ":
            console.print("Cell already occupied. Choose a different cell.")
            continue
        board[row][col] = player
        valid_move = True

# Function to get computer's move
def get_computer_move(board, player):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = player

# Function to check for a winner or a tie
def check_winner(board, players):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    if all(cell != " " for row in board for cell in row):
        return "Tie"
    return None

# Main function to encapsulate game logic
def main():
    board, human, computer = initialize_game()
    
    while True:
        display_board(board)
        get_human_move(board, human)
        
        winner = check_winner(board, [human, computer])
        if winner:
            console.print(f"{winner} is the winner!" if winner != "Tie" else "It's a tie!")
            break
        
        get_computer_move(board, computer)
        
        winner = check_winner(board, [human, computer])
        if winner:
            console.print(f"{winner} is the winner!" if winner != "Tie" else "It's a tie!")
            break

if __name__ == "__main__":
    main()
