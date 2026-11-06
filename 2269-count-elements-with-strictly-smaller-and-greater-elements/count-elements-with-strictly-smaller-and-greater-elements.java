class Solution {
    public int countElements(int[] nums) {
        int mn = Integer.MAX_VALUE, mx = Integer.MIN_VALUE;
        for (int x : nums) {
            mn = Math.min(mn, x);
            mx = Math.max(mx, x);
        }
        int count = 0;
        for (int x : nums)
            if (x > mn && x < mx) count++;
        return count;
    }
}