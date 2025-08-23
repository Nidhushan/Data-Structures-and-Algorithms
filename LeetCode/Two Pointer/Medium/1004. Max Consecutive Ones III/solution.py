class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            
        return right - left + 1
        
        # left = 0
        # zeros = 0
        # max_count = 0

        # for right, x in enumerate(nums):
        #     if x == 0:
        #         zeros+=1
        #     while zeros>k:
        #         if nums[left] == 0:
        #             zeros-=1
        #         left+=1
        #     max_count = max(max_count, right-left+1)
        # return max_count
        
        # max_count = 0
        # left = 0
        # right = 0
        # N = len(nums)
        # flips = k
        # while right<N:
        #     if nums[right] == 0:
        #         if flips > 0:
        #             flips -= 1
        #         else:
        #             while nums[left] == 1:
        #                 left += 1
        #             left += 1
        #     max_count = max(max_count, right - left + 1)
        #     right += 1
        # return max_count

                
        


        """
        Question:
        nums - List[int]
        k - int
        return max consecutive 1's if k 0's can be flipped to 1

        Solution:
        Two Pointer:
        when you encounter a 0, decrement k till you exhaust k
        """