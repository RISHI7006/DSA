class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0   # max money if we stop before the previous house (dp[i-2])
        curr = 0   # max money considering up to the previous house (dp[i-1])
        
        for num in nums:
            # Either skip this house (keep curr) or rob it (prev + num)
            prev, curr = curr, max(curr, prev + num)
        
        return curr