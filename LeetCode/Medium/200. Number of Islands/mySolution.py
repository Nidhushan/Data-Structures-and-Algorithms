class Solution:
    def killIsland(self, grid, i, j, m, n):
        if i<0 or j<0 or i>=m or j>=n or grid[i][j]=='0':
            return
        grid[i][j] = '0'
        self.killIsland(grid, i+1, j, m, n)
        self.killIsland(grid, i, j-1, m, n)
        self.killIsland(grid, i, j+1, m, n)
        self.killIsland(grid, i-1, j, m, n)

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.killIsland(grid, i, j, m, n)
                    ans+=1
                
        return ans