class Solution:
    def mostWordsFound(self, sentences):
        max_words = 0

        for sentence in sentences:
            words = sentence.count(' ') + 1
            max_words = max(max_words, words)

        return max_words