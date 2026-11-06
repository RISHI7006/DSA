class Solution:
    def countElements(self, nums: List[int]) -> int:
        mn, mx = min(nums), max(nums)
        return sum(1 for x in nums if mn < x < mx)