class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int rows = grid.size(), cols = grid[0].size();
        queue<pair<int,int>> q;
        int freshCount = 0;
        
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 2) {
                    q.push({r, c});
                } else if (grid[r][c] == 1) {
                    freshCount++;
                }
            }
        }
        
        if (freshCount == 0) return 0;
        
        int minutes = 0;
        vector<pair<int,int>> dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        
        while (!q.empty()) {
            int levelSize = q.size();
            bool rottedAny = false;
            
            // Process one full "minute" (BFS level) at a time
            for (int i = 0; i < levelSize; i++) {
                auto [r, c] = q.front();
                q.pop();
                
                for (auto& [dr, dc] : dirs) {
                    int nr = r + dr, nc = c + dc;
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2;
                        freshCount--;
                        rottedAny = true;
                        q.push({nr, nc});
                    }
                }
            }
            
            if (rottedAny) minutes++;
        }
        
        return freshCount == 0 ? minutes : -1;
    }
};