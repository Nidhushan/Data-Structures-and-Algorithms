class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        max_sum = 0
        curr_sum = 0
        left = 0

        for right, x in enumerate(nums):
            while x in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left+=1
            seen.add(x)
            curr_sum+=x
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
        
        # di = {}
        # max_sum = 0
        # curr_sum = 0
        # left = 0

        # for right, x in enumerate(nums):
        #     di[x] = di.get(x, 0) + 1
        #     curr_sum += x
        #     while di[x]>1:
        #         di[nums[left]] -= 1
        #         curr_sum -= nums[left]
        #         left+=1
            
        #     max_sum = max(max_sum, curr_sum)
        
        # return max_sum

        """
        Question:
        nums - List[int]
        return maximum sum of unique subarray

        Solution:
        hashmap stores to maintain uniqueness
        use two pointers, return sum of the max subarray
        """