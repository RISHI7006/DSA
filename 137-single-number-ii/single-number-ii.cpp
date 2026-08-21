class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ones = 0;   // bits that have appeared once (mod 3)
        int twos = 0;   // bits that have appeared twice (mod 3)

        for (int num : nums) {
            // Add num to twos if it's already in ones
            twos |= ones & num;

            // Add num to ones (XOR toggles the bits)
            ones ^= num;

            // If a bit has appeared three times, remove it from both
            int threes = ones & twos;
            ones &= ~threes;
            twos &= ~threes;
        }

        return ones;
    }
};