class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = [0] * 501
        for x in arr:
            count[x] += 1
        for v in range(500, 0, -1):
            if count[v] == v:
                return v
        return -1
        