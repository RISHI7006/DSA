class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int c1 = 0, c2 = 0;   // do candidates
        int n1 = 0, n2 = 0;   // unke counters

        // Pass 1: candidates dhundo
        for (int x : nums) {
            if (n1 > 0 && x == c1) n1++;          // c1 se match
            else if (n2 > 0 && x == c2) n2++;     // c2 se match
            else if (n1 == 0) { c1 = x; n1 = 1; } // c1 khali, naya candidate
            else if (n2 == 0) { c2 = x; n2 = 1; } // c2 khali, naya candidate
            else { n1--; n2--; }                  // teeno alag, dono ghatao
        }

        // Pass 2: asli count karke verify karo
        n1 = 0; n2 = 0;
        for (int x : nums) {
            if (x == c1) n1++;
            else if (x == c2) n2++;
        }

        vector<int> res;
        int limit = nums.size() / 3;
        if (n1 > limit) res.push_back(c1);
        if (n2 > limit) res.push_back(c2);
        return res;
    }
};