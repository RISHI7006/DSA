class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        last = len(nums) - 1

        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= last:
                return True

        return True