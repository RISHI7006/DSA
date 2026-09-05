class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        
        def box_index(r, c):
            return (r // 3) * 3 + c // 3
        
        # Initialize bitmasks
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    digit = int(board[r][c]) - 1
                    mask = 1 << digit
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[box_index(r, c)] |= mask
        
        def backtrack(row, col):
            if row == 9:
                return True
            
            next_row, next_col = (row + 1, 0) if col == 8 else (row, col + 1)
            
            if board[row][col] != '.':
                return backtrack(next_row, next_col)
            
            b = box_index(row, col)
            used = rows[row] | cols[col] | boxes[b]
            
            for digit in range(9):
                mask = 1 << digit
                if used & mask:
                    continue
                
                # Place digit
                board[row][col] = str(digit + 1)
                rows[row] |= mask
                cols[col] |= mask
                boxes[b] |= mask
                
                if backtrack(next_row, next_col):
                    return True
                
                # Backtrack
                board[row][col] = '.'
                rows[row] &= ~mask
                cols[col] &= ~mask
                boxes[b] &= ~mask
            
            return False
        
        backtrack(0, 0)