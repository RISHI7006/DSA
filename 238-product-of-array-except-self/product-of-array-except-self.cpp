class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> answer(n, 1);

        // First pass: compute prefix products
        // answer[i] = product of all elements to the left of i
        int prefix = 1;
        for (int i = 0; i < n; i++) {
            answer[i] = prefix;
            prefix *= nums[i];
        }

        // Second pass: multiply by suffix products
        // answer[i] *= product of all elements to the right of i
        int suffix = 1;
        for (int i = n - 1; i >= 0; i--) {
            answer[i] *= suffix;
            suffix *= nums[i];
        }

        return answer;
    }
};