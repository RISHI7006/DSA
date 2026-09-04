class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        cols = set()          # columns with a queen
        diag1 = set()         # "/" diagonals (row - col is constant)
        diag2 = set()         # "\" diagonals (row + col is constant)
        board = [['.'] * n for _ in range(n)]

        def backtrack(row: int) -> None:
            if row == n:
                # Convert board to the required string format
                result.append([''.join(r) for r in board])
                return

            for col in range(n):
                # Check if this position conflicts with any existing queen
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # Place the queen
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                board[row][col] = 'Q'

                backtrack(row + 1)

                # Backtrack: remove the queen
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
                board[row][col] = '.'

        backtrack(0)
        return result