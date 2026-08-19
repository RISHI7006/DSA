class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for char in s:
            if char == '*':
                stack.pop()  # remove the closest non-star to the left
            else:
                stack.append(char)  # add non-star character

        return ''.join(stack)