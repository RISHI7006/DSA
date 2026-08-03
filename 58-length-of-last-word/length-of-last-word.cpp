class Solution {
public:
    int lengthOfLastWord(string s) {
        int i = s.size() - 1;

        // Step 1: skip trailing spaces
        while (i >= 0 && s[i] == ' ') {
            i--;
        }

        // Step 2: count characters of the last word
        int length = 0;
        while (i >= 0 && s[i] != ' ') {
            length++;
            i--;
        }

        return length;
    }
};