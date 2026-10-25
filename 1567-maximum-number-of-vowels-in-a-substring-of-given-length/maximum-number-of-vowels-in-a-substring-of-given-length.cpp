class Solution {
public:
    int maxVowels(string s, int k) {
        auto isV = [](char c) {
            return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        };

        int n = s.size(), cnt = 0;
        for (int i = 0; i < k; i++) cnt += isV(s[i]);

        int best = cnt;
        for (int i = k; i < n && best < k; i++) {
            cnt += isV(s[i]) - isV(s[i - k]);
            if (cnt > best) best = cnt;
        }

        return best;
    }
};