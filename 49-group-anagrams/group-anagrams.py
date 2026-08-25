from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        for s in strs:
            # Count frequency of each character (26 lowercase letters)
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1

            # Use tuple of counts as the key (lists aren't hashable)
            key = tuple(count)
            groups[key].append(s)

        return list(groups.values())