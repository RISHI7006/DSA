class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string result;
        result.reserve(word1.size() + word2.size());  // avoid reallocations
        
        int i = 0, j = 0;

        // Alternate taking characters from both strings
        while (i < word1.size() && j < word2.size()) {
            result += word1[i];
            result += word2[j];
            i++;
            j++;
        }

        // Append remaining characters from word1
        while (i < word1.size()) {
            result += word1[i];
            i++;
        }

        // Append remaining characters from word2
        while (j < word2.size()) {
            result += word2[j];
            j++;
        }

        return result;
    }
};