class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<vector<int>> res;

        // Use long long throughout to avoid overflow (values up to 1e9, sums up to 4e9)
        long long tgt = target;

        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            long long minSum1 = (long long)nums[i] + nums[i+1] + nums[i+2] + nums[i+3];
            if (minSum1 > tgt) break;

            long long maxSum1 = (long long)nums[i] + nums[n-3] + nums[n-2] + nums[n-1];
            if (maxSum1 < tgt) continue;

            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;

                long long minSum2 = (long long)nums[i] + nums[j] + nums[j+1] + nums[j+2];
                if (minSum2 > tgt) break;

                long long maxSum2 = (long long)nums[i] + nums[j] + nums[n-2] + nums[n-1];
                if (maxSum2 < tgt) continue;

                int left = j + 1, right = n - 1;
                while (left < right) {
                    long long total = (long long)nums[i] + nums[j] + nums[left] + nums[right];

                    if (total == tgt) {
                        res.push_back({nums[i], nums[j], nums[left], nums[right]});
                        left++;
                        right--;
                        while (left < right && nums[left] == nums[left - 1]) left++;
                        while (left < right && nums[right] == nums[right + 1]) right--;
                    } else if (total < tgt) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }

        return res;
    }
};