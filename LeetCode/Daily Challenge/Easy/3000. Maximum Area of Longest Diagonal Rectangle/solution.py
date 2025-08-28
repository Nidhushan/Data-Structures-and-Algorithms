class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = 0
        ans_ind = 0
        for i, (l, b) in enumerate(dimensions):
            x = math.sqrt(l*l + b*b)
            if x>max_diag:
                ans_ind = i
                max_diag = x
            elif x == max_diag:
                if l*b > dimensions[ans_ind][0]*dimensions[ans_ind][1]:
                    ans_ind = i

        return dimensions[ans_ind][0] * dimensions[ans_ind][1]