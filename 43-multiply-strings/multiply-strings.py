class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m):
            a = ord(num1[i]) - 48
            for j in range(n):
                res[i + j + 1] += a * (ord(num2[j]) - 48)

        for k in range(m + n - 1, 0, -1):
            res[k - 1] += res[k] // 10
            res[k] %= 10

        start = 1 if res[0] == 0 else 0
        return "".join(map(str, res[start:]))