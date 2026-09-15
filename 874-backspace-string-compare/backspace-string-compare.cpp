class Solution {
public:
    bool backspaceCompare(string s, string t) {
        auto build = [](const string& str) {
            string stack;
            for (char ch : str) {
                if (ch != '#') {
                    stack.push_back(ch);
                } else if (!stack.empty()) {
                    stack.pop_back();
                }
            }
            return stack;
        };
        
        return build(s) == build(t);
    }
};