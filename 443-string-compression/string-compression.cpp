class Solution {
public:
    int compress(vector<char>& chars) {
        int write = 0, i = 0;
        
        while (i < chars.size()) {
            char c = chars[i];
            int cnt = 0;
            while (i < chars.size() && chars[i] == c) {
                cnt++;
                i++;
            }
            
            chars[write++] = c;
            
            if (cnt > 1) {
                string s = to_string(cnt);
                for (char ch : s) {
                    chars[write++] = ch;
                }
            }
        }
        
        return write;
    }
};