class Solution {
    public int findLucky(int[] arr) {
        int[] count = new int[501];
        for (int x : arr) count[x]++;
        for (int v = 500; v >= 1; v--)
            if (count[v] == v) return v;
        return -1;
    }
}