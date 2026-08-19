class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int k = 0; // position where next non-zero should go

        // First pass: move all non-zero elements to the front
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != 0) {
                nums[k] = nums[i];
                k++;
            }
        }

        // Second pass: fill remaining positions with zeros
        while (k < nums.size()) {
            nums[k] = 0;
            k++;
        }
    }
};