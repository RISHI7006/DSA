class Solution {
    public int arrangeCoins(int n) {
        long x = 8L * n + 1;
        long s = (long) Math.sqrt((double) x);
        while (s * s > x) s--;
        while ((s + 1) * (s + 1) <= x) s++;
        return (int) ((s - 1) / 2);
    }
}