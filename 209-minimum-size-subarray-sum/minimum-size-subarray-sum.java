class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length, best = n + 1;
        long total = 0;
        int l = 0;

        for (int r = 0; r < n; r++) {
            total += nums[r];
            while (total >= target) {
                best = Math.min(best, r - l + 1);
                total -= nums[l++];
            }
        }
        return best == n + 1 ? 0 : best;
    }
}