class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Step 1: skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        if i == n:
            return 0

        # Step 2: sign
        sign = 1
        if s[i] == '+' or s[i] == '-':
            if s[i] == '-':
                sign = -1
            i += 1

        # Step 3: read digits
        num = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # clamp early to avoid huge integer growth (Python ints are unbounded)
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        num *= sign

        # Step 4: clamp to 32-bit range (redundant given early clamp, but safe)
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num