class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int l = 0, r = nums.size() - 1, count = 0;

        while (l < r) {
            long long s = (long long)nums[l] + nums[r];
            if (s == k) {
                count++;
                l++;
                r--;
            } else if (s < k) {
                l++;
            } else {
                r--;
            }
        }
        return count;
    }
};