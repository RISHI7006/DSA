class Solution {
    public int appendCharacters(String s, String t) {
        int j = 0, m = t.length();
        for (int i = 0; i < s.length() && j < m; i++) {
            if (s.charAt(i) == t.charAt(j)) j++;
        }
        return m - j;
    }
}