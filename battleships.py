import random

def create_board(size):
    return [['~' for _ in range(size)] for _ in range(size)]

def print_board(board):
    print("  " + " ".join(str(i) for i in range(len(board))))
    for i, row in enumerate(board):
        print(f"{i} " + " ".join(row))

def place_ship(board, length):
    placed = False
    while not placed:
        orientation = random.choice(['H', 'V'])
        if orientation == 'H':
            row = random.randint(0, len(board) - 1)
            col = random.randint(0, len(board) - length)
            if all(board[row][c] == '~' for c in range(col, col + length)):
                for c in range(col, col + length):
                    board[row][c] = 'S'
                placed = True
        else:
            row = random.randint(0, len(board) - length)
            col = random.randint(0, len(board) - 1)
            if all(board[r][col] == '~' for r in range(row, row + length)):
                for r in range(row, row + length):
                    board[r][col] = 'S'
                placed = True

def place_all_ships(board, ship_lengths):
    for length in ship_lengths:
        place_ship(board, length)

def check_guess(board, row, col):
    try:
        row = int(row)
        col = int(col)
    except ValueError:
        return "Invalid input. Please enter a number.", False
    if row < 0 or row >= len(board) or col < 0 or col >= len(board):
        return "Off-grid guess!", False
    if board[row][col] == 'S':
        board[row][col] = 'X'
        return "Hit!", True
    elif board[row][col] == '~':
        board[row][col] = 'O'
        return "Miss!", True
    else:
        return "Already guessed.", False

def all_ships_sunk(board):
    return not any('S' in row for row in board)

def get_grid_size():
    while True:
        try:
            size = int(input("Enter the grid size (minimum 5): "))
            if size < 5:
                print("Grid size must be at least 5.")
            else:
                return size
        except ValueError:
            print("Please enter a valid number.")

def play_game():
    size = get_grid_size()
    board = create_board(size)
    ship_lengths = [2, 3, 3, 4, 5][:min(5, size - 1)]
    place_all_ships(board, ship_lengths)

    guesses = 0
    while not all_ships_sunk(board):
        print_board(board)
        row = input(f"Enter row (0-{size-1}) or 'q' to quit: ")
        if row.lower() == 'q':
            print("Thanks for playing!")
            return
        col = input(f"Enter column (0-{size-1}): ")
        result, valid = check_guess(board, row, col)
        print(result)
        if valid:
            guesses += 1
    
    print(f"All ships sunk in {guesses} guesses!")

if __name__ == "__main__":
    play_game()