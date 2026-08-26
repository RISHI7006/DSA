class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        doubled = (s + s)[1:-1]
        return s in doubled