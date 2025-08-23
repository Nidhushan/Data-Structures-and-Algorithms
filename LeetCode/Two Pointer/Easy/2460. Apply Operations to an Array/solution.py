class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        N = len(nums)

        for i in range(N-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        left = 0

        for right in range(N):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1

        return nums
            

        """
        Question:
        nums - List[int]
        apply the operations and return the resulting array

        Solution:
        loop through and apply first operation
        shift all 0's to end using two pointer
        """