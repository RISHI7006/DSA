class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        increasing = True
        decreasing = True

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                decreasing = False  # we saw an increase, can't be decreasing
            if nums[i] > nums[i + 1]:
                increasing = False  # we saw a decrease, can't be increasing

        return increasing or decreasing