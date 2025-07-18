class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        return -1 if len(nums) < 3 else sum(nums[:3]) - min(nums[:3]) - max(nums[:3])
        
        # if len(nums)<3:
        #     return -1
        
        # temp = nums[:3]
        # x = max(nums)
        # y = min(nums)
        # for i in nums:
        #     if i!=x and i!=y:
        #         return i