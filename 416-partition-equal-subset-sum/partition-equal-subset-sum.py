class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        # Odd total can never be split into two equal integer sums
        if total % 2 != 0:
            return False
        
        target = total // 2
        # dp[s] = True if some subset of nums seen so far sums to exactly s
        dp = [False] * (target + 1)
        dp[0] = True  # empty subset sums to 0
        
        for num in nums:
            # Traverse backwards to avoid reusing the same num twice in one iteration
            for s in range(target, num - 1, -1):
                if dp[s - num]:
                    dp[s] = True
            # Early exit optimization: if target already reachable, stop early
            if dp[target]:
                return True
        
        return dp[target]