class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size())
            return findMedianSortedArrays(nums2, nums1);

        int m = nums1.size(), n = nums2.size();
        int half = (m + n + 1) / 2;

        int lo = 0, hi = m;
        const int INF = INT_MAX;

        while (lo <= hi) {
            int i = lo + (hi - lo) / 2;
            int j = half - i;

            int left1  = (i > 0) ? nums1[i - 1] : INT_MIN;
            int right1 = (i < m) ? nums1[i]     : INF;
            int left2  = (j > 0) ? nums2[j - 1] : INT_MIN;
            int right2 = (j < n) ? nums2[j]     : INF;

            if (left1 <= right2 && left2 <= right1) {
                if ((m + n) % 2 == 1)
                    return max(left1, left2);
                else
                    return (max(left1, left2) + min(right1, right2)) / 2.0;
            } else if (left1 > right2) {
                hi = i - 1;
            } else {
                lo = i + 1;
            }
        }

        return -1.0; // unreachable if inputs valid
    }
};