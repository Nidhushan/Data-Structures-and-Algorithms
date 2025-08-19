class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)

        for i, n in enumerate(nums):
            dp[i] = max(n, dp[i-1]+n)
        
        return max(dp)

        # max_sum = nums[0]
        # cur_sum = 0

        # for i in range(len(nums)):
        #     if cur_sum<0:
        #         cur_sum = 0
            
        #     cur_sum += nums[i]
        #     max_sum = max(max_sum, cur_sum)