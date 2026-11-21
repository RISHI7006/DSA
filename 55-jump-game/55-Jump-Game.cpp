class Solution {
public:
    bool canJump(vector<int>& nums) {
        int farthest = 0, last = nums.size() - 1;

        for (int i = 0; i <= last; i++) {
            if (i > farthest) return false;
            farthest = max(farthest, i + nums[i]);
            if (farthest >= last) return true;
        }
        return true;
    }
};