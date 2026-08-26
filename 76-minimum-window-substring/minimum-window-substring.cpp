class Solution {
public:
    string minWindow(string s, string t) {
        if (s.empty() || t.empty() || s.size() < t.size()) return "";

        int need[128] = {0};
        for (char c : t) {
            need[c]++;
        }

        int required = 0;
        for (int i = 0; i < 128; i++) {
            if (need[i] > 0) required++;
        }

        int window[128] = {0};
        int formed = 0;
        int left = 0, right = 0;
        int minLen = INT_MAX, minLeft = 0;

        int sLen = s.size();

        while (right < sLen) {
            char c = s[right];
            window[c]++;

            if (need[c] > 0 && window[c] == need[c]) {
                formed++;
            }

            while (formed == required) {
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    minLeft = left;
                }

                char leftChar = s[left];
                window[leftChar]--;
                if (need[leftChar] > 0 && window[leftChar] < need[leftChar]) {
                    formed--;
                }
                left++;
            }

            right++;
        }

        return minLen == INT_MAX ? "" : s.substr(minLeft, minLen);
    }
};