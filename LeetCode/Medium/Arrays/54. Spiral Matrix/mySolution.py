class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret= []

        while matrix:
            # step 1 - add first row
            ret += matrix.pop(0)

            # step 2 - add last column
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())

            # step 3 - add last row in reverse
            if matrix:
                ret += matrix.pop()[::-1]

            # step 4 - add first column in reverse
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))

        return ret