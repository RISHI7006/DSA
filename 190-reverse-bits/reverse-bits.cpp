class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t result = 0;
        for (int i = 0; i < 32; i++) {
            // Extract the i-th bit from n (from the right)
            uint32_t bit = (n >> i) & 1;
            // Place it at the mirrored position (31 - i) from the right
            result |= (bit << (31 - i));
        }
        return result;
    }
};