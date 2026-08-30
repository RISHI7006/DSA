class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # stores indices, monotonic decreasing temperatures

        for i in range(n):
            # While current temp is warmer than the temp at stack's top index
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_idx = stack.pop()
                answer[prev_idx] = i - prev_idx  # days waited

            stack.append(i)

        return answer