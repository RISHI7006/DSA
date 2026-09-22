class Solution {
public:
    string makeGood(string s) {
        string stack;
        
        for (char ch : s) {
            // If the top of the stack is the "opposite case" of ch, they cancel out
            if (!stack.empty() && stack.back() != ch && 
                tolower(stack.back()) == tolower(ch)) {
                stack.pop_back();
            } else {
                stack.push_back(ch);
            }
        }
        
        return stack;
    }
};