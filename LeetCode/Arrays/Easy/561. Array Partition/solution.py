class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        sum = 0
        for i in range(0,len(nums), 2):
            sum+=nums[i]
        return sum
    