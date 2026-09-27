class Solution {
public:
    bool detectCapitalUse(string word) {
        int upper = 0;

        for (char ch : word) {
            if (isupper(ch)) {
                upper++;
            }
        }

        if (upper == 0) {
            return true;
        }

        if (upper == word.length()) {
            return true;
        }

        if (upper == 1 && isupper(word[0])) {
            return true;
        }

        return false;
    }
};