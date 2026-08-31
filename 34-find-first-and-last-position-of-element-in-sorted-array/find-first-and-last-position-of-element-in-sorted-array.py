class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left_bound = self.findBound(nums, target, True)

        if left_bound == -1:
            return [-1, -1]

        right_bound = self.findBound(nums, target, False)

        return [left_bound, right_bound]

    def findBound(self, nums: list[int], target: int, find_first: bool) -> int:
        left, right = 0, len(nums) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                result = mid
                if find_first:
                    right = mid - 1  # keep searching left for an earlier occurrence
                else:
                    left = mid + 1   # keep searching right for a later occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result
        