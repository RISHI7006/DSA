class Solution:
    def maxLength(self, arr):
        masks = []

        for word in arr:
            mask = 0
            valid = True

            for ch in word:
                bit = 1 << (ord(ch) - ord('a'))

                if mask & bit:
                    valid = False
                    break

                mask |= bit

            if valid:
                masks.append((mask, len(word)))

        def backtrack(index, mask, length):
            nonlocal ans

            if length > ans:
                ans = length

            for i in range(index, len(masks)):
                new_mask, word_len = masks[i]

                if mask & new_mask == 0:
                    backtrack(
                        i + 1,
                        mask | new_mask,
                        length + word_len
                    )

        ans = 0
        backtrack(0, 0, 0)

        return ans