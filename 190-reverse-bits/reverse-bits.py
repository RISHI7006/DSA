class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # Extract the i-th bit from n (from the right)
            bit = (n >> i) & 1
            # Place it at the mirrored position (31 - i) from the right
            result |= (bit << (31 - i))
        return result