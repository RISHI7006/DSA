class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0, right = (int)s.size() - 1;

        while (left < right) {
            // Skip non-alphanumeric from the left
            while (left < right && !isalnum((unsigned char)s[left])) {
                left++;
            }
            // Skip non-alphanumeric from the right
            while (left < right && !isalnum((unsigned char)s[right])) {
                right--;
            }

            if (tolower((unsigned char)s[left]) != tolower((unsigned char)s[right])) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }
};