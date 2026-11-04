class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    continue
                keys = [(ch, 'r', r), (ch, 'c', c), (ch, 'b', r // 3, c // 3)]
                if any(k in seen for k in keys):
                    return False
                seen.update(keys)
        return True