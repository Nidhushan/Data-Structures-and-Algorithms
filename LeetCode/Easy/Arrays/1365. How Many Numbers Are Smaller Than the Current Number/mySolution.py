class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        di = {}
        li = []
        for i, v in enumerate(temp):
            if v not in di:
                di[v] = i

        for i in nums:
            li.append(di[i])

        return li