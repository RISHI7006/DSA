class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        maxCount = 0

        for num in nums:
            if num == 1:
                count += 1
                if count > maxCount:
                    maxCount = count
            else:
                count = 0

        return maxCount
        