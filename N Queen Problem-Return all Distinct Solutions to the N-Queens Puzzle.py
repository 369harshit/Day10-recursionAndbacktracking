def solve_n_queens(n):
    solutions = []  # List to store all distinct solutions

    def backtrack(board, row):
        # Base case: all queens have been placed
        if row == n:
            solutions.append(board[:])  # Add a copy of the current board to solutions
            return

        for col in range(n):
            if is_valid(board, row, col):
                # Place the queen in the current position
                board[row] = col

                # Recur for the next row
                backtrack(board, row + 1)

                # Clear the queen position (backtracking)
                board[row] = -1

    def is_valid(board, row, col):
        # Check if it's safe to place a queen in the current position
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    # Initialize the chessboard with -1 (no queen)
    board = [-1] * n

    # Start the backtracking from the first row
    backtrack(board, 0)

    return solutions

# Function to print the solutions with queens represented by 'q' and empty spaces by '.'
def print_solutions(solutions):
    for sol in solutions:
        for row in sol:
            line = ['.'] * len(sol)
            line[row] = 'q'
            print(' '.join(line))
        print()

# Test the solve_n_queens function
n = 4
solutions = solve_n_queens(n)
print_solutions(solutions)
print("Total solutions:", len(solutions))
