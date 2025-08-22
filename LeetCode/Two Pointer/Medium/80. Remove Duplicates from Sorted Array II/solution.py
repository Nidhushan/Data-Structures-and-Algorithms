class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        if N<2:
            return N
        j = 2
        for i in range(2, N):
            if nums[i] != nums[j-2]:
                nums[j] = nums[i]
                j+=1
        return j

        # N = len(nums)
        # i = 2
        # while i<N:
        #     j=i
        #     if nums[i] == nums[i-1] and nums[i-1] == nums[i-2]:
        #         del(nums[i])
        #         N-=1
        #     else:
        #         i+=1

        """
        Question:
        nums -> List[int]
        remove duplicates allowing upto 2 in place

        Solution:
        if condition to check 2nd duplicate:
            delete if found
        """ 