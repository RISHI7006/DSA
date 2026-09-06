class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> tails; // tails[i] = smallest possible tail value of an increasing subsequence of length i+1
        
        for (int num : nums) {
            // Binary search for the leftmost position where num can replace/extend
            auto it = lower_bound(tails.begin(), tails.end(), num);
            
            if (it == tails.end()) {
                tails.push_back(num); // num extends the longest subsequence found so far
            } else {
                *it = num; // num replaces an element to keep tails as small as possible
            }
        }
        
        return tails.size();
    }
};