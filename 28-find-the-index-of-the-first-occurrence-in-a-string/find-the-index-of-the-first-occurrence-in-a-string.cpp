class Solution {
public:
    int strStr(string haystack, string needle) {
        int n = haystack.size(), m = needle.size();
        if (m == 0) return 0;

        // Build LPS array
        vector<int> lps(m, 0);
        int length = 0, i = 1;
        while (i < m) {
            if (needle[i] == needle[length]) {
                lps[i++] = ++length;
            } else if (length != 0) {
                length = lps[length - 1];
            } else {
                lps[i++] = 0;
            }
        }

        // Search
        i = 0;
        int j = 0;
        while (i < n) {
            if (haystack[i] == needle[j]) {
                i++; j++;
                if (j == m) return i - j;
            } else if (j != 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
        return -1;
    }
};