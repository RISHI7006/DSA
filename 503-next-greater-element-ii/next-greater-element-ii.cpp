class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n, -1);
        stack<int> stk;  // stores indices

        for (int i = 0; i < 2 * n; i++) {
            int idx = i % n;

            while (!stk.empty() && nums[stk.top()] < nums[idx]) {
                result[stk.top()] = nums[idx];
                stk.pop();
            }

            if (i < n) {
                stk.push(idx);
            }
        }

        return result;
    }
};