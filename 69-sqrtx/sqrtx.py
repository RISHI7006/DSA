class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        lo, hi = 1, x // 2  # sqrt(x) <= x/2 for x >= 4
        ans = 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            sq = mid * mid

            if sq == x:
                return mid
            elif sq < x:
                ans = mid       # mid is a valid candidate, try for bigger
                lo = mid + 1
            else:
                hi = mid - 1

        return ans