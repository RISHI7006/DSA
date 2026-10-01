class Solution:
    def maxLength(self, arr):
        masks = []

        for word in arr:
            mask = 0
            for c in word:
                bit = 1 << (ord(c) - 97)
                if mask & bit:
                    break
                mask |= bit
            else:
                masks.append((mask, len(word)))

        ans = 0
        stack = [(0, 0, 0)]

        while stack:
            i, mask, length = stack.pop()

            if length > ans:
                ans = length

            for j in range(i, len(masks)):
                m, l = masks[j]

                if not (mask & m):
                    stack.append((j + 1, mask | m, length + l))

        return ans