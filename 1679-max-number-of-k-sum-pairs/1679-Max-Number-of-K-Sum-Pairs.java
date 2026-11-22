class Solution {
    public int maxOperations(int[] nums, int k) {
        Arrays.sort(nums);
        int l = 0, r = nums.length - 1, count = 0;

        while (l < r) {
            long s = (long) nums[l] + nums[r];
            if (s == k) {
                count++;
                l++;
                r--;
            } else if (s < k) {
                l++;
            } else {
                r--;
            }
        }
        return count;
    }
}