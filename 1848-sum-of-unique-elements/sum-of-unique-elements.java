class Solution {
    public int sumOfUnique(int[] nums) {
        int[] freq = new int[101];
        for (int x : nums) freq[x]++;
        int sum = 0;
        for (int v = 1; v <= 100; v++) {
            if (freq[v] == 1) sum += v;
        }
        return sum;
    }
}