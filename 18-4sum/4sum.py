class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            # Skip duplicate first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Prune: smallest possible sum from here is too big
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # Prune: largest possible sum from here is too small
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicate second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # Prune: smallest possible sum for this i,j is too big
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                # Prune: largest possible sum for this i,j is too small
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # Skip duplicates for third element
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        # Skip duplicates for fourth element
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return res