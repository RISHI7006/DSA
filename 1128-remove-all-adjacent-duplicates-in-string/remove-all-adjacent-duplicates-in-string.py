class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()  # remove the adjacent duplicate
            else:
                stack.append(char)  # add the character

        return ''.join(stack)