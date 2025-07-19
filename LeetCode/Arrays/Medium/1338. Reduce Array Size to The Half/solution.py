class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = int(len(arr)/2)
        di = {}
        s = ()
        for i in arr:
            di[i] = di.get(i, 0) + 1
        freq = sorted(di.values(), reverse=True)
        res = 0
        for f in freq:
            n-=f
            res+=1
            if n<=0:
                break
        
        return res