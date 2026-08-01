class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0

        while left < right:
            h = min(height[left], height[right])
            width = right - left
            best = max(best, h * width)

            # Move the pointer at the shorter line inward;
            # moving the taller one can only shrink or maintain the limiting height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return best
        