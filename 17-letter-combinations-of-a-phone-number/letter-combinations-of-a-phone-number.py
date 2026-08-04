class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }

        res = []
        path = []

        def backtrack(idx: int) -> None:
            if idx == len(digits):
                res.append(''.join(path))
                return

            for ch in phone[digits[idx]]:
                path.append(ch)
                backtrack(idx + 1)
                path.pop()  # undo choice, try next letter

        backtrack(0)
        return res