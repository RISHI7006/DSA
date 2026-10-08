class Solution {
public:
    string reverseWords(string s) {
        // Step 1: reverse the whole string
        reverse(s.begin(), s.end());

        int n = s.size();
        int write = 0;  // where the next cleaned character goes

        for (int read = 0; read < n; read++) {
            if (s[read] != ' ') {
                // Add a single space between words (not before the first word)
                if (write != 0) s[write++] = ' ';

                // Copy the word, then reverse it back to correct orientation
                int start = write;
                while (read < n && s[read] != ' ') {
                    s[write++] = s[read++];
                }
                reverse(s.begin() + start, s.begin() + write);
            }
        }

        s.resize(write);  // drop leftover characters
        return s;
    }
};