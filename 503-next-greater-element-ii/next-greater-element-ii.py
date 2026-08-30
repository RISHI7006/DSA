class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [-1] * n
        stack = []  # stores indices, monotonic decreasing values

        # Iterate 2n times to simulate circular traversal
        for i in range(2 * n):
            idx = i % n

            while stack and nums[stack[-1]] < nums[idx]:
                result[stack.pop()] = nums[idx]

            # Only push indices during the first pass to avoid duplicate processing
            if i < n:
                stack.append(idx)

        return result
        