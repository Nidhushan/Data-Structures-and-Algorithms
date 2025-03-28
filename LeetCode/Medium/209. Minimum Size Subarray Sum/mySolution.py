class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        total = 0
        l = 0

        for i in range(len(nums)):

            total+=nums[i]

            while total>=target:

                res = min(res, i-l+1)

                total-=nums[l]
                l+=1
            
        if res == float('inf'):
            return 0
        return res
        
