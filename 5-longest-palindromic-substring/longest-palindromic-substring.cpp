class Solution {
public:
    string longestPalindrome(string s) {
        int start = 0, maxLen = 1;
        int n = s.size();

        auto expand = [&](int left, int right) {
            while (left >= 0 && right < n && s[left] == s[right]) {
                left--;
                right++;
            }
            left++;
            right--;
            if (right - left + 1 > maxLen) {
                maxLen = right - left + 1;
                start = left;
            }
        };

        for (int i = 0; i < n; i++) {
            expand(i, i);       // Odd length
            expand(i, i + 1);   // Even length
        }

        return s.substr(start, maxLen);
    }
};