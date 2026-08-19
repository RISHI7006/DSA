class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0  # position where next non-zero should go

        # First pass: move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1

        # Second pass: fill remaining positions with zeros
        while k < len(nums):
            nums[k] = 0
            k += 1