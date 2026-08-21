class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0  # pointer for word1
        j = 0  # pointer for word2

        # Alternate taking characters from both strings
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1

        # Append remaining characters from word1 (if any)
        while i < len(word1):
            result.append(word1[i])
            i += 1

        # Append remaining characters from word2 (if any)
        while j < len(word2):
            result.append(word2[j])
            j += 1

        return ''.join(result)
        