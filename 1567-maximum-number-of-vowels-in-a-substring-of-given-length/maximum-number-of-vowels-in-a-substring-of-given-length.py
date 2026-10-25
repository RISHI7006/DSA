class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        cnt = 0
        for i in range(k):
            if s[i] in vowels:
                cnt += 1
        best = cnt

        for i in range(k, len(s)):
            if s[i] in vowels:
                cnt += 1
            if s[i - k] in vowels:
                cnt -= 1
            if cnt > best:
                best = cnt
                if best == k:
                    break

        return best