from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Count characters needed from t
        need = Counter(t)
        required = len(need)  # number of unique characters we need to satisfy

        # Sliding window pointers
        left = 0
        formed = 0  # number of unique characters currently satisfied
        window_counts = {}

        # Result tracking: (window length, left, right)
        result = float('inf'), None, None

        right = 0
        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            # Check if this character's frequency matches the requirement
            if char in need and window_counts[char] == need[char]:
                formed += 1

            # Try to contract the window from the left while it's still valid
            while left <= right and formed == required:
                char = s[left]

                # Update result if this window is smaller
                if right - left + 1 < result[0]:
                    result = (right - left + 1, left, right)

                # Remove the leftmost character from the window
                window_counts[char] -= 1
                if char in need and window_counts[char] < need[char]:
                    formed -= 1

                left += 1

            right += 1

        return "" if result[0] == float('inf') else s[result[1]:result[2] + 1]