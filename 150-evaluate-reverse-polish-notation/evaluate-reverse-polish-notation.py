class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token in operators:
                # Pop two operands (order matters for - and /)
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:  # division
                    # Truncate toward zero (Python's // rounds toward -inf, so use int() on true division)
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[0]
        