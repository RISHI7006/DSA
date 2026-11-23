class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        m = len(t)
        for ch in s:
            if j < m and ch == t[j]:
                j += 1
        return m - j