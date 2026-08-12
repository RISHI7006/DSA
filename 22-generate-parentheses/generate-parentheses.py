class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        path = []

        def backtrack(open_count: int, close_count: int) -> None:
            if len(path) == 2 * n:
                res.append(''.join(path))
                return

            # Can add '(' as long as we haven't used all n opens
            if open_count < n:
                path.append('(')
                backtrack(open_count + 1, close_count)
                path.pop()

            # Can add ')' only if it wouldn't create more closes than opens
            if close_count < open_count:
                path.append(')')
                backtrack(open_count, close_count + 1)
                path.pop()

        backtrack(0, 0)
        return res