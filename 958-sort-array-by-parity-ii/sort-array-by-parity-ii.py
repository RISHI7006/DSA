class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        j = 1  # pointer over odd indices
        for i in range(0, len(nums), 2):
            if nums[i] & 1:  # odd value at an even index
                while nums[j] & 1:  # find an even value at an odd index
                    j += 2
                nums[i], nums[j] = nums[j], nums[i]
        return nums
        