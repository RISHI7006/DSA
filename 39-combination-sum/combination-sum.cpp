class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> result;
        vector<int> path;

        backtrack(candidates, target, 0, path, result);
        return result;
    }

private:
    void backtrack(vector<int>& candidates, int remaining, int start,
                    vector<int>& path, vector<vector<int>>& result) {
        if (remaining == 0) {
            result.push_back(path);
            return;
        }

        for (int i = start; i < candidates.size(); i++) {
            if (candidates[i] > remaining) {
                break;  // pruning: no point checking larger candidates
            }

            path.push_back(candidates[i]);
            backtrack(candidates, remaining - candidates[i], i, path, result);
            path.pop_back();
        }
    }
};