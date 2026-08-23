class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        // Sort by start time
        sort(intervals.begin(), intervals.end());

        vector<vector<int>> result;
        result.push_back(intervals[0]);

        for (int i = 1; i < intervals.size(); i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];
            int lastStart = result.back()[0];
            int lastEnd = result.back()[1];

            // If current interval overlaps with the last merged interval
            if (start <= lastEnd) {
                // Merge by extending the end
                result.back()[1] = max(lastEnd, end);
            } else {
                // No overlap, add as new interval
                result.push_back({start, end});
            }
        }

        return result;
    }
};