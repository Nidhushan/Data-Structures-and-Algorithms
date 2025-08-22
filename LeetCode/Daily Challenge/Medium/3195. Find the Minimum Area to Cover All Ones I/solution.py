class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        if int(sum(val for row in grid for val in row) == 1):
            return 1
        r = len(grid)
        c = len(grid[0])
        top = bot = right = 0
        left = float("inf")
        first = True
        for i in range(r):
            for j in range(c):
                if first and grid[i][j] == 1:
                    top = i
                    first = False
                if grid[i][j] == 1:
                    bot = i+1
                
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    left = min(left, j) 
                    right = max(right, j)
        right +=1
        
        print(top, bot, left, right)
        return (bot-top)*(right - left)

