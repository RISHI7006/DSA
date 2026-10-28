class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int n = arr.length, target = k * threshold, s = 0, cnt = 0;

        for (int i = 0; i < k; i++) s += arr[i];
        if (s >= target) cnt++;

        for (int i = k; i < n; i++) {
            s += arr[i] - arr[i - k];
            if (s >= target) cnt++;
        }

        return cnt;
    }
}