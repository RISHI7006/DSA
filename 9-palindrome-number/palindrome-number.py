class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers aren't palindromes; numbers ending in 0 (except 0 itself) aren't either
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x //= 10

        # Even digit count: x == reverted
        # Odd digit count: middle digit doesn't matter, so drop it via reverted // 10
        return x == reverted or x == reverted // 10
        