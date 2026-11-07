class Solution:
    def arrangeCoins(self, n: int) -> int:
        from math import isqrt
        return (isqrt(8 * n + 1) - 1) // 2