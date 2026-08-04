class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};

        static const vector<string> phone = {
            "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
        };

        vector<string> res;
        string path;
        path.reserve(digits.size());

        backtrack(digits, 0, phone, path, res);
        return res;
    }

private:
    void backtrack(const string& digits, int idx, const vector<string>& phone,
                    string& path, vector<string>& res) {
        if (idx == (int)digits.size()) {
            res.push_back(path);
            return;
        }

        const string& letters = phone[digits[idx] - '0'];
        for (char ch : letters) {
            path.push_back(ch);
            backtrack(digits, idx + 1, phone, path, res);
            path.pop_back(); // undo choice, try next letter
        }
    }
};