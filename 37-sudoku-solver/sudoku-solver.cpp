class Solution {
public:
    int rows[9] = {0}, cols[9] = {0}, boxes[9] = {0};
    
    void solveSudoku(vector<vector<char>>& board) {
        // Initialize bitmasks: bit k set means digit (k+1) is used
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    int digit = board[i][j] - '1'; // 0-indexed digit
                    int mask = 1 << digit;
                    rows[i] |= mask;
                    cols[j] |= mask;
                    boxes[(i/3)*3 + j/3] |= mask;
                }
            }
        }
        backtrack(board, 0, 0);
    }
    
    bool backtrack(vector<vector<char>>& board, int row, int col) {
        if (row == 9) return true;
        
        int nextRow = (col == 8) ? row + 1 : row;
        int nextCol = (col == 8) ? 0 : col + 1;
        
        if (board[row][col] != '.') {
            return backtrack(board, nextRow, nextCol);
        }
        
        int b = (row/3)*3 + col/3;
        int used = rows[row] | cols[col] | boxes[b];
        
        for (int digit = 0; digit < 9; digit++) {
            int mask = 1 << digit;
            if (used & mask) continue; // digit already used
            
            // Place digit
            board[row][col] = '1' + digit;
            rows[row] |= mask;
            cols[col] |= mask;
            boxes[b] |= mask;
            
            if (backtrack(board, nextRow, nextCol)) return true;
            
            // Backtrack
            board[row][col] = '.';
            rows[row] &= ~mask;
            cols[col] &= ~mask;
            boxes[b] &= ~mask;
        }
        
        return false;
    }
};