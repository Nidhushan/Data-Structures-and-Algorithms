class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        di = {}
        for i in nums:
            di[i] = di.get(i, 0) + 1
        sum = 0
        for k, v in di.items():
            if v==1:
                sum+=k
        return sum
        # print(di)