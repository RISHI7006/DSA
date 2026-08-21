class Solution {
public:
    string removeDuplicates(string s) {
        string stack;

        for (char c : s) {
            if (!stack.empty() && stack.back() == c) {
                stack.pop_back();  // remove the adjacent duplicate
            } else {
                stack.push_back(c);  // add the character
            }
        }

        return stack;
    }
};