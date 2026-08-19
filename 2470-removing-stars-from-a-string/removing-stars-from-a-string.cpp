class Solution {
public:
    string removeStars(string s) {
        string stack;

        for (char c : s) {
            if (c == '*') {
                stack.pop_back();  // remove the closest non-star to the left
            } else {
                stack.push_back(c);  // add non-star character
            }
        }

        return stack;
    }
};