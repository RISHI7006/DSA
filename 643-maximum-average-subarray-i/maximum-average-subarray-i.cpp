
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int windowSum = 0;

        // Calculate the first window sum
        for (int i = 0; i < k; i++) {
            windowSum += nums[i];
        }

        int maxSum = windowSum;

        // Slide the window
        for (int i = k; i < nums.size(); i++) {
            windowSum += nums[i] - nums[i - k];
            maxSum = max(maxSum, windowSum);
        }

        return (double)maxSum / k;
    }
};
