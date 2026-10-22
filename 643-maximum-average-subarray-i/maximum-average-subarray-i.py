class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum = 0

        for i in range(k):
            window_sum += nums[i]

        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k
