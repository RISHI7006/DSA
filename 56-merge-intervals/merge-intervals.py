class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Sort by start time
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        for start, end in intervals[1:]:
            last_start, last_end = result[-1]

            # If current interval overlaps with the last merged interval
            if start <= last_end:
                # Merge by extending the end
                result[-1][1] = max(last_end, end)
            else:
                # No overlap, add as new interval
                result.append([start, end])

        return result