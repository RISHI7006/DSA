class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)

        # Case 1: three largest numbers
        product1 = nums[n - 1] * nums[n - 2] * nums[n - 3]

        # Case 2: two smallest (most negative) + one largest
        # Two negatives multiply to a large positive
        product2 = nums[0] * nums[1] * nums[n - 1]

        return max(product1, product2)