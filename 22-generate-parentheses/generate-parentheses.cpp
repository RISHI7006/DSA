class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string path;
        path.reserve(2 * n);

        backtrack(n, 0, 0, path, res);
        return res;
    }

private:
    void backtrack(int n, int openCount, int closeCount, string& path, vector<string>& res) {
        if ((int)path.size() == 2 * n) {
            res.push_back(path);
            return;
        }

        if (openCount < n) {
            path.push_back('(');
            backtrack(n, openCount + 1, closeCount, path, res);
            path.pop_back();
        }

        if (closeCount < openCount) {
            path.push_back(')');
            backtrack(n, openCount, closeCount + 1, path, res);
            path.pop_back();
        }
    }
};