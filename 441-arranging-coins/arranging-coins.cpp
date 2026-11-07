class Solution {
public:
    int arrangeCoins(int n) {
        long long x = 8LL * n + 1;
        long long s = (long long)sqrt((double)x);
        while (s * s > x) s--;
        while ((s + 1) * (s + 1) <= x) s++;
        return (int)((s - 1) / 2);
    }
};