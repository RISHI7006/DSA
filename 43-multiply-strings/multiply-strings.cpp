class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") return "0";

        int m = num1.size(), n = num2.size();
        vector<int> res(m + n, 0);

        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int total = (num1[i] - '0') * (num2[j] - '0') + res[i + j + 1];
                res[i + j + 1] = total % 10;
                res[i + j] += total / 10;
            }
        }

        string ans;
        for (int d : res) {
            if (ans.empty() && d == 0) continue;
            ans.push_back(d + '0');
        }
        return ans;
    }
};