class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Total moves = (m-1) downs + (n-1) rights
        # Answer = C(m+n-2, m-1)
        result = 1
        # Compute C(m+n-2, min(m-1, n-1)) to minimize iterations
        N = m + n - 2
        k = min(m - 1, n - 1)
        for i in range(1, k + 1):
            result = result * (N - k + i) // i
        return result