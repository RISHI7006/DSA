class Solution {
    public int maxVowels(String s, int k) {
        int n = s.length(), cnt = 0;

        for (int i = 0; i < k; i++)
            if (isV(s.charAt(i))) cnt++;

        int best = cnt;
        for (int i = k; i < n && best < k; i++) {
            if (isV(s.charAt(i))) cnt++;
            if (isV(s.charAt(i - k))) cnt--;
            if (cnt > best) best = cnt;
        }

        return best;
    }

    private boolean isV(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}