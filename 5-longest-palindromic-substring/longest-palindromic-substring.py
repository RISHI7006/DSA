class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        if n < 2:
            return s

        start = 0
        maxLen = 1

        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - left - 1

        for i in range(n):
            l, length = expand(i, i)
            if length > maxLen:
                start = l
                maxLen = length

            l, length = expand(i, i + 1)
            if length > maxLen:
                start = l
                maxLen = length

        return s[start:start + maxLen]