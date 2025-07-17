class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sum = 0

        for i in range(n):
            print(mat[i][i], mat[i][n-i-1])
            sum += mat[i][i] + mat[i][n-i-1]
        
        if n%2!=0:
            sum -= mat[int((n-1)/2)][int((n-1)/2)]
            # print(mat[mid][mid])
        return sum