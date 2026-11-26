
class Solution {
public:
    long long minCost(vector<int>& nums) {

        int n = nums.size();

        long long ans = 1LL * nums[0] + nums[n - 1];

        long long negSum = 0;
        long long closestNeg = LLONG_MIN;
        long long minPos = LLONG_MAX;

        int negCount = 0;
        bool hasZero = false;

        for (int i = 1; i < n - 1; i++) {

            long long x = nums[i];

            if (x < 0) {
                negSum += x;
                negCount++;
                closestNeg = max(closestNeg, x);
            }
            else if (x > 0) {
                minPos = min(minPos, x);
            }
            else {
                hasZero = true;
            }
        }

        ans += negSum;

        if (negCount % 2 == 1) {

            long long penalty;

            if (hasZero) {
                penalty = 0;
            }
            else {
                penalty = min(-closestNeg, minPos);
            }

            ans += penalty;
        }

        return ans;
    }
};
