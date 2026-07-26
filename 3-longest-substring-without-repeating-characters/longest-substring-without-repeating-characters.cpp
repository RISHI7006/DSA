class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> last_seen(128, -1);  // ASCII index -> last seen position
        int left = 0, max_len = 0;
        int n = s.size();

        for (int right = 0; right < n; ++right) {
            int idx = s[right];
            if (last_seen[idx] >= left) {
                left = last_seen[idx] + 1;
            }
            last_seen[idx] = right;
            max_len = max(max_len, right - left + 1);
        }

        return max_len;
    }
};