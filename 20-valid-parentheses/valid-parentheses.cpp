class Solution {
public:
    bool isValid(string s) {
        int n = s.size();
        if (n % 2 != 0) return false;  // odd length can never be valid
        
        // Use a fixed-size array as stack instead of std::stack (faster)
        char stack[10001];
        int top = -1;
        
        for (int i = 0; i < n; i++) {
            char c = s[i];
            if (c == '(' || c == '[' || c == '{') {
                stack[++top] = c;
            } else {
                if (top == -1) return false;
                char t = stack[top];
                if ((c == ')' && t != '(') ||
                    (c == ']' && t != '[') ||
                    (c == '}' && t != '{')) {
                    return false;
                }
                top--;
            }
        }
        
        return top == -1;
    }
};