class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& nums) {
        int n = nums.size();
        int j = 1;
        for (int i = 0; i < n; i += 2) {
            if (nums[i] & 1) {
                while (nums[j] & 1) j += 2;
                swap(nums[i], nums[j]);
            }
        }
        return nums;
    }
};