class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();

        // Case 1: three largest numbers
        long long product1 = (long long)nums[n - 1] * nums[n - 2] * nums[n - 3];

        // Case 2: two smallest (most negative) + one largest
        long long product2 = (long long)nums[0] * nums[1] * nums[n - 1];

        return (int)max(product1, product2);
    }
};