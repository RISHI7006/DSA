class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;

        unordered_set<int> num_set(nums.begin(), nums.end());
        int longestStreak = 0;

        for (int num : num_set) {
            // Only start counting from the beginning of a sequence
            if (num_set.find(num - 1) == num_set.end()) {
                int currentNum = num;
                int currentStreak = 1;

                // Count the consecutive sequence length
                while (num_set.find(currentNum + 1) != num_set.end()) {
                    currentNum++;
                    currentStreak++;
                }

                longestStreak = max(longestStreak, currentStreak);
            }
        }

        return longestStreak;
    }
};