class Solution:
    # Precompute reversal for all 256 possible byte values (done once, shared across calls)
    cache = {}
    
    def reverseBits(self, n: int) -> int:
        if not self.cache:
            for byte in range(256):
                rev = 0
                for i in range(8):
                    rev |= ((byte >> i) & 1) << (7 - i)
                self.cache[byte] = rev
        
        result = 0
        for i in range(4):
            byte = (n >> (8 * i)) & 0xFF
            result |= (self.cache[byte] << (24 - 8 * i))
        return result