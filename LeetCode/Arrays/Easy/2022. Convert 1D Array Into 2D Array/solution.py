class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []

        arr_2d = []

        for i in range(m):
            arr_2d.append(original[i*n:(i+1)*n])
        
        return arr_2d