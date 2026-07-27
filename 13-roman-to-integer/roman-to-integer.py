class Solution:
    def romanToInt(self, s: str) -> int:
        val = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        result = 0
        n = len(s)
        
        for i in range(n):
            if i + 1 < n and val[s[i]] < val[s[i+1]]:
                result -= val[s[i]]
            else:
                result += val[s[i]]
        
        return result