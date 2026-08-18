class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        result = 0
        
        # XOR all numbers from 0 to n
        for i in range(len(nums) + 1):
            result ^= i
        
        # XOR all numbers in the array
        for num in nums:
            result ^= num
        
        return result

        