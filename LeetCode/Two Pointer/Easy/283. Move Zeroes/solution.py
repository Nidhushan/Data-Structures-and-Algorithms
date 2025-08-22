class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        left = 0
        # right = 0

        for right in range(N):
            if nums[right]!=0:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1

        """

        loop through the list:
            if curVal != 0:
                swap right and left
                increment left
            increment right
        """
        
        # N = len(nums)

        # for i in range(N-1):
        #     if nums[i]==0:
        #         j=i+1
        #         while j<N-1:
        #             if nums[j]!=0:
        #                 break
        #             j+=1
        #         nums[i], nums[j] = nums[j], nums[i]

        """
        Question:
        nums --> List

        Move all 0's in nums to the end of the array

        nums = [0,1,0,3,12]
        Output: [1,3,12,0,0]

        Loop through the list:
            if i is 0:
                swap with next non zero
            
        """
        