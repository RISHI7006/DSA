class Solution {
    public int minimumRecolors(String blocks, int k) {
        int n = blocks.length(), whites = 0;

        for (int i = 0; i < k; i++)
            if (blocks.charAt(i) == 'W') whites++;

        int best = whites;

        for (int i = k; i < n && best > 0; i++) {
            if (blocks.charAt(i) == 'W') whites++;
            if (blocks.charAt(i - k) == 'W') whites--;
            if (whites < best) best = whites;
        }

        return best;
    }
}