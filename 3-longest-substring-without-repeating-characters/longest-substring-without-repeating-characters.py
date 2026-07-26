class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = [-1] * 128
        left = 0
        max_len = 0

        for right in range(len(s)):
            idx = ord(s[right])
            if last_seen[idx] >= left:
                left = last_seen[idx] + 1
            last_seen[idx] = right
            if right - left + 1 > max_len:
                max_len = right - left + 1

        return max_len
        