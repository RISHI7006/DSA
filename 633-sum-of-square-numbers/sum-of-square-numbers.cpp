class Solution {
public:
    bool judgeSquareSum(long long c) {
        long long a = 0;
        long long b = (long long)sqrt(c);

        while (a <= b) {
            long long sqSum = a * a + b * b;

            if (sqSum == c) {
                return true;
            } else if (sqSum < c) {
                a++; // need a larger sum
            } else {
                b--; // need a smaller sum
            }
        }

        return false;
    }
};