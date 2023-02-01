#!/usr/bin/python3
"""
Module 101-nqueens
"""
import sys

def solve_nqueens(n):
    def can_place(row, col):
        # Check if a queen can be placed in cell (row, col)
        for i in range(row):
            if board[i] == col or \
               abs(board[i] - col) == abs(i - row):
                return False
        return True

    def nqueens_helper(row):
        if row == n:
            result.append(board[:])
            return

        for col in range(n):
            if can_place(row, col):
                board[row] = col
                nqueens_helper(row + 1)

    result = []
    board = [-1] * n
    nqueens_helper(0)
    return result

def print_solutions(solutions, n):
    for solution in solutions:
        print(" ".join(["." * i + "Q" + "." * (n-i-1) for i in solution]))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(n)
    print_solutions(solutions, n)

