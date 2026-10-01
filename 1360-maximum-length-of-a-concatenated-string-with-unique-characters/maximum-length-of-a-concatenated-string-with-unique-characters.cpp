class Solution {
public:
    int ans = 0;

    void backtrack(vector<pair<int, int>>& masks,
                   int index,
                   int mask,
                   int length) {

        ans = max(ans, length);

        for (int i = index; i < masks.size(); i++) {

            int newMask = masks[i].first;
            int wordLen = masks[i].second;

            if ((mask & newMask) == 0) {
                backtrack(
                    masks,
                    i + 1,
                    mask | newMask,
                    length + wordLen
                );
            }
        }
    }

    int maxLength(vector<string>& arr) {
        vector<pair<int, int>> masks;

        for (string word : arr) {
            int mask = 0;
            bool valid = true;

            for (char ch : word) {
                int bit = 1 << (ch - 'a');

                if (mask & bit) {
                    valid = false;
                    break;
                }

                mask |= bit;
            }

            if (valid) {
                masks.push_back({mask, (int)word.length()});
            }
        }

        backtrack(masks, 0, 0, 0);

        return ans;
    }
};