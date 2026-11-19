class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int mx = *max_element(candies.begin(), candies.end());
        vector<bool> result;
        for (int c : candies)
            result.push_back(c + extraCandies >= mx);
        return result;
    }
};