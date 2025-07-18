class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        temp = []
        for i in arr:
            if i==0:
                temp.append(i)
                temp.append(i)
            else:
                temp.append(i)
        arr[:] = temp[:len(arr)]


