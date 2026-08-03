class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int best = nums[0] + nums[1] + nums[2];

        for (int i = 0; i < n - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue; // skip duplicate anchors

            int left = i + 1, right = n - 1;

            while (left < right) {
                int currSum = nums[i] + nums[left] + nums[right];

                if (abs(currSum - target) < abs(best - target)) {
                    best = currSum;
                }

                if (currSum == target) {
                    return currSum; // exact match, can't do better
                } else if (currSum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return best;
    }
};