class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, columns = len(grid), len(grid[0])

        islands = 0

        def dfs(r, c):
            
            # Out of Bounds or Water
            if ((r < 0 or r >= rows) or
                (c < 0 or c >= columns) or
                grid[r][c] == '0'):
                return None
            
            # Mark it Visited
            grid[r][c] = "0"

            # Explore 4 Directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            
            for c in range(columns):
                
                if grid[r][c] == '1':
                    
                    islands += 1
                    
                    dfs(r, c)
        
        return islands
