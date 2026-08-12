class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle overflow edge case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign of result
        negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values (use positive space to avoid INT_MIN edge issues)
        dvd = abs(dividend)
        dvs = abs(divisor)

        quotient = 0

        # For each bit position, find the largest shift such that (dvs << shift) <= dvd
        while dvd >= dvs:
            temp = dvs
            multiple = 1
            while (temp << 1) <= dvd:
                temp <<= 1
                multiple <<= 1
            dvd -= temp
            quotient += multiple

        result = -quotient if negative else quotient

        # Clamp to 32-bit range
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        return result