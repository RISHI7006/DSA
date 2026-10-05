class Solution {
public:
    int countSegments(string s) {
        int count = 0;
        bool inSegment = false;

        for (char c : s) {
            if (c != ' ') {
                if (!inSegment) {
                    count++;
                    inSegment = true;
                }
            } else {
                inSegment = false;
            }
        }

        return count;
    }
};