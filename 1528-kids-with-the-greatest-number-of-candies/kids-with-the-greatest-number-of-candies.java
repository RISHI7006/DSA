class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int mx = 0;
        for (int c : candies) mx = Math.max(mx, c);

        List<Boolean> result = new ArrayList<>();
        for (int c : candies)
            result.add(c + extraCandies >= mx);
        return result;
    }
}