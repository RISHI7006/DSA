class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0   # bits that have appeared once (mod 3)
        twos = 0   # bits that have appeared twice (mod 3)

        for num in nums:
            # Add num to twos if it's already in ones
            twos |= ones & num

            # Add num to ones (XOR toggles the bits)
            ones ^= num

            # If a bit has appeared three times, remove it from both
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes

        return ones
        