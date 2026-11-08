class Solution {
    public boolean checkIfPangram(String sentence) {
        int mask = 0;
        for (char c : sentence.toCharArray()) {
            mask |= 1 << (c - 'a');
        }
        return mask == (1 << 26) - 1;
    }
}