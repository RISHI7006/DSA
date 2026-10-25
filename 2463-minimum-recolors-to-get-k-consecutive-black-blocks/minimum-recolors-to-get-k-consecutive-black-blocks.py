class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = blocks[:k].count('W')
        best = whites

        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                whites += 1
            if blocks[i - k] == 'W':
                whites -= 1
            if whites < best:
                best = whites
                if best == 0:
                    break

        return best