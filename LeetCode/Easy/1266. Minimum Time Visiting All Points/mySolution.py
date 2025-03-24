class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        x, y = points.pop()
        while points:
            x1, y1 = points.pop()
            res += max(abs(x-x1), abs(y-y1))
            x, y = x1, y1
        
        return res