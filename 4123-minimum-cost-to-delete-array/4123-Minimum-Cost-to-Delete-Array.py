
class Solution:
    def minCost(self, nums: List[int]) -> int:
        n = len(nums)

        ans = nums[0] + nums[-1]

        neg_sum = 0
        neg_count = 0
        closest_neg = float('-inf')
        min_pos = float('inf')
        has_zero = False

        for x in nums[1:-1]:

            if x < 0:
                neg_sum += x
                neg_count += 1
                closest_neg = max(closest_neg, x)

            elif x > 0:
                min_pos = min(min_pos, x)

            else:
                has_zero = True

        ans += neg_sum

        if neg_count % 2 == 1:

            if has_zero:
                penalty = 0
            else:
                penalty = min(-closest_neg, min_pos)

            ans += penalty

        return ans
