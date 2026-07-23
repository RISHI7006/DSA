class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]  # ← must be indented one more level
            seen[num] = i

        return []

      