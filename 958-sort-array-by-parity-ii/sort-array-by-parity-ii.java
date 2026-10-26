class Solution {
    public int[] sortArrayByParityII(int[] nums) {
        int n = nums.length, j = 1;
        for (int i = 0; i < n; i += 2) {
            if ((nums[i] & 1) == 1) {
                while ((nums[j] & 1) == 1) j += 2;
                int t = nums[i];
                nums[i] = nums[j];
                nums[j] = t;
            }
        }
        return nums;
    }
}