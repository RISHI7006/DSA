class Solution {
    public boolean canJump(int[] nums) {
        int farthest = 0, last = nums.length - 1;

        for (int i = 0; i <= last; i++) {
            if (i > farthest) return false;
            farthest = Math.max(farthest, i + nums[i]);
            if (farthest >= last) return true;
        }
        return true;
    }
}