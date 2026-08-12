class Solution {
public:
    int divide(int dividend, int divisor) {
        const int INT_MAX_V = INT_MAX;
        const int INT_MIN_V = INT_MIN;

        // Handle overflow edge case
        if (dividend == INT_MIN_V && divisor == -1) {
            return INT_MAX_V;
        }

        bool negative = (dividend < 0) != (divisor < 0);

        // Use long long and abs to safely handle INT_MIN (whose abs overflows int)
        long long dvd = llabs((long long)dividend);
        long long dvs = llabs((long long)divisor);

        long long quotient = 0;

        while (dvd >= dvs) {
            long long temp = dvs;
            long long multiple = 1;

            while ((temp << 1) <= dvd) {
                temp <<= 1;
                multiple <<= 1;
            }

            dvd -= temp;
            quotient += multiple;
        }

        long long result = negative ? -quotient : quotient;

        // Clamp to 32-bit range
        if (result > INT_MAX_V) return INT_MAX_V;
        if (result < INT_MIN_V) return INT_MIN_V;
        return (int)result;
    }
};