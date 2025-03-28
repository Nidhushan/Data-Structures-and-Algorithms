class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mad = 100000000
        res = []
        for i in range(len(arr)-1):
            if abs(arr[i+1]-arr[i])<mad:
                res = []
                mad = abs(arr[i+1]-arr[i])
                res.append([arr[i], arr[i+1]])
            
            elif abs(arr[i+1]-arr[i])==mad:
                res.append([arr[i], arr[i+1]])
        return res