class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1, c2 = None, None
        n1, n2 = 0, 0

        # Pass 1: candidates dhundo
        for x in nums:
            if x == c1:
                n1 += 1
            elif x == c2:
                n2 += 1
            elif n1 == 0:
                c1, n1 = x, 1
            elif n2 == 0:
                c2, n2 = x, 1
            else:
                n1 -= 1
                n2 -= 1

        # Pass 2: verify karo
        n1 = n2 = 0
        for x in nums:
            if x == c1:
                n1 += 1
            elif x == c2:
                n2 += 1

        res = []
        limit = len(nums) // 3
        if n1 > limit:
            res.append(c1)
        if n2 > limit:
            res.append(c2)
        return res