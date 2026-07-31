class Solution {
public:
    string convert(string s, int numRows) {
        int n = s.size();
        if (numRows == 1 || numRows >= n) return s;

        string res;
        res.reserve(n); // avoid reallocations -> less memory churn

        int cycle = 2 * numRows - 2;

        for (int row = 0; row < numRows; row++) {
            if (row == 0 || row == numRows - 1) {
                for (int i = row; i < n; i += cycle)
                    res.push_back(s[i]);
            } else {
                for (int i = row; i < n; i += cycle) {
                    res.push_back(s[i]);
                    int j = i + cycle - 2 * row;
                    if (j < n) res.push_back(s[j]);
                }
            }
        }

        return res;
    }
};