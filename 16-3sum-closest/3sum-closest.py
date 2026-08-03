class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = nums[0] + nums[1] + nums[2]  # initial guess

        for i in range(n - 2):
            # Optional pruning: skip duplicate anchors to avoid redundant work
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if abs(curr_sum - target) < abs(best - target):
                    best = curr_sum

                if curr_sum == target:
                    return curr_sum  # can't get closer than exact match
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return best