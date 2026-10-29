class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        for (int x : nums) {
            int i = abs(x) - 1;
            if (nums[i] > 0) nums[i] = -nums[i];
        }
        vector<int> res;
        for (int i = 0; i < (int)nums.size(); i++)
            if (nums[i] > 0) res.push_back(i + 1);
        return res;
    }
};