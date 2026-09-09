class Solution {
public:
    int rows, cols;
    
    void dfs(vector<vector<char>>& grid, int r, int c) {
        // Base case: out of bounds or water/already-visited
        if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] != '1') {
            return;
        }
        
        // Mark as visited by sinking the land (avoids extra visited set)
        grid[r][c] = '0';
        
        // Explore all 4 directions
        dfs(grid, r + 1, c);
        dfs(grid, r - 1, c);
        dfs(grid, r, c + 1);
        dfs(grid, r, c - 1);
    }
    
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) return 0;
        
        rows = grid.size();
        cols = grid[0].size();
        int count = 0;
        
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1') {
                    count++;
                    dfs(grid, r, c); // sink the entire connected island
                }
            }
        }
        
        return count;
    }
};