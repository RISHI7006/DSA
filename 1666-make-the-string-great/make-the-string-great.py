class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for ch in s:
            # If the top of the stack is the "opposite case" of ch, they cancel out
            if stack and stack[-1] != ch and stack[-1].lower() == ch.lower():
                stack.pop()
            else:
                stack.append(ch)
        
        return ''.join(stack)