class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                max_count = max(max_count, right-left)
                left = right+1
        max_count = max(max_count, len(nums)-left)
        return max_count
       
        # max_count = 0
        # count = 0
        # for i in nums:
        #     if i==1:
        #         count+=1
        #     else:
        #         count = 0
        #     if count>max_count:
        #         max_count = count
            
        # return max_count

        """
        Question:
        nums - List[int]
        return max consecutive no of 1's

        Solution:
        BruteForce: increment count for each 1 and return max instance of count
        two poinetr: might be complicating things? But you can have a left pointer, increment right till its a 1, then for 0 update the pointers

        """
        