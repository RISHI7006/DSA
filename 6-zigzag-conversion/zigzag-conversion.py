class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or numRows >= n:
            return s

        res = []
        cycle = 2 * numRows - 2  # full zigzag period

        for row in range(numRows):
            if row == 0 or row == numRows - 1:
                # only vertical hits, spaced by cycle
                for i in range(row, n, cycle):
                    res.append(s[i])
            else:
                # alternate between "down" and "diagonal up" hits
                i = row
                while i < n:
                    res.append(s[i])
                    j = i + cycle - 2 * row  # diagonal partner
                    if j < n:
                        res.append(s[j])
                    i += cycle

        return ''.join(res)
        