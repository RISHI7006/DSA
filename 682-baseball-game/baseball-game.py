class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for op in operations:
            if op == '+':
                # Sum of the previous two scores
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                # Double of the previous score
                stack.append(2 * stack[-1])
            elif op == 'C':
                # Invalidate and remove the previous score
                stack.pop()
            else:
                # It's an integer score
                stack.append(int(op))
        
        return sum(stack)