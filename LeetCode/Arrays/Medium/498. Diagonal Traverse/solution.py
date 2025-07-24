class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        r, c = len(mat)-1, len(mat[0])-1
        di = {}
        for i in range(r+1):
            for j in range(c+1):
                if i+j not in di:
                    di[i+j] = [mat[i][j]]
                else:
                    di[i+j].append(mat[i][j])
        
        res = []

        for item in di.items():
            if item[0]%2==0:
                [res.append(x) for x in item[1][::-1]]
            else:
                [res.append(x) for x in item[1]]
        
        return res