class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> path;

        function<void(int)> backtrack = [&](int start) {
            ans.push_back(path);

            for (int i = start; i < nums.size(); i++) {
                path.push_back(nums[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };

        backtrack(0);
        return ans;
    }
};