class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        bool increasing = true;
        bool decreasing = true;

        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums[i] < nums[i + 1]) {
                decreasing = false;  // saw an increase
            }
            if (nums[i] > nums[i + 1]) {
                increasing = false;  // saw a decrease
            }
        }

        return increasing || decreasing;
    }
};