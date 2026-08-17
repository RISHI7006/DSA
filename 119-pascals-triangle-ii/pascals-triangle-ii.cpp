class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> row = {1};

        for (int i = 1; i <= rowIndex; i++) {
            row.push_back(0); // extend with a 0

            // Update backwards
            for (int j = i; j >= 1; j--) {
                row[j] = row[j] + row[j - 1];
            }
        }

        return row;
    }
};