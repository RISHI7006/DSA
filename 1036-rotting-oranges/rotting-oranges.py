class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Find all initially rotten oranges (sources) and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, minute)
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0  # no fresh oranges to begin with
        
        minutes_elapsed = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while queue:
            r, c, minute = queue.popleft()
            minutes_elapsed = max(minutes_elapsed, minute)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # rot it
                    fresh_count -= 1
                    queue.append((nr, nc, minute + 1))
        
        # If any fresh oranges remain unreached, it's impossible
        return minutes_elapsed if fresh_count == 0 else -1
        