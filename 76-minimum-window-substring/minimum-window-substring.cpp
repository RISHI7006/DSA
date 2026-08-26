class Solution {
public:
    string minWindow(string s, string t) {
        if (s.empty() || t.empty()) return "";

        unordered_map<char, int> need;
        for (char c : t) {
            need[c]++;
        }

        int required = need.size();
        int left = 0, formed = 0;
        unordered_map<char, int> windowCounts;

        int minLen = INT_MAX, minLeft = 0;

        int right = 0;
        while (right < s.size()) {
            char c = s[right];
            windowCounts[c]++;

            if (need.count(c) && windowCounts[c] == need[c]) {
                formed++;
            }

            while (left <= right && formed == required) {
                char leftChar = s[left];

                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    minLeft = left;
                }

                windowCounts[leftChar]--;
                if (need.count(leftChar) && windowCounts[leftChar] < need[leftChar]) {
                    formed--;
                }

                left++;
            }

            right++;
        }

        return minLen == INT_MAX ? "" : s.substr(minLeft, minLen);
    }
};