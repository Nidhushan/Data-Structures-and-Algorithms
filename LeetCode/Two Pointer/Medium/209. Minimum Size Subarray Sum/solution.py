class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len
            
        
        
        # res = float('inf')
        # total = 0
        # l = 0

        # for i in range(len(nums)):

        #     total+=nums[i]

        #     while total>=target:

        #         res = min(res, i-l+1)

        #         total-=nums[l]
        #         l+=1
            
        # if res == float('inf'):
        #     return 0
        # return res
        
        """
        Question:
        nums - List[int]
        target - int
        return len(smallest subarray) whose sum<=target

        Solution:
        Sliding window, make sure the sum of the window>=target
        return smallest len of window
        """