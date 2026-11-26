class Solution {
public:
    vector<vector<int>> res;
    vector<int> path;

    void dfs(vector<int>& c, int start, int remaining) {
        if (remaining == 0) {
            res.push_back(path);
            return;
        }
        for (int i = start; i < c.size(); i++) {
            if (i > start && c[i] == c[i - 1]) continue;
            if (c[i] > remaining) break;
            path.push_back(c[i]);
            dfs(c, i + 1, remaining - c[i]);
            path.pop_back();
        }
    }

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        dfs(candidates, 0, target);
        return res;
    }
};