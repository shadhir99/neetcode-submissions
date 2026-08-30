class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, columns = len(grid), len(grid[0])
        
        islands = 0

        def bfs(r, c):

            queue = deque()
            
            queue.append([r, c])

            grid[r][c] = '0'

            while queue:

                row, col = queue.popleft()

                directions = [[1, 0],
                              [-1, 0],
                              [0, 1], 
                              [0, -1]]
                
                for dr, dc in directions:
                    
                    new_row = row + dr
                    new_col = col + dc

                    if ((0 <= new_row < rows) and
                        (0 <= new_col < columns) and
                        grid[new_row][new_col] == '1'):

                        grid[new_row][new_col] = '0'
                    
                        queue.append([new_row, new_col])
            
        
        for r in range(rows):
            
            for c in range(columns):
                
                if grid[r][c] == '1':
                    
                    islands += 1

                    bfs(r, c)
        
        return islands
                    