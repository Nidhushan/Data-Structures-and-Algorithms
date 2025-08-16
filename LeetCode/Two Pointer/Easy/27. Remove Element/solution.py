class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j+=1
        
        return j
        
        # N = len(nums)
        # left, right = 0, N-1
        # count = 0
        
        # while left<=right:
        #     if nums[left] == val:
        #         nums[left] = nums[right]
        #         right-=1
        #     else:
        #         left += 1
        
        # return left
        


        
        # N = len(nums)
        # j=0
        # i=0
        # while i<N:
        #     if nums[i] == val:
        #         j = i
        #         while j<N-1:
        #             nums[j] = nums[j+1]
        #             j+=1
        #         N-=1
        #     else:
        #         i+=1
        # return  N


        # j = 0  # points to position to write next valid element

        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[j] = nums[i]
        #         j += 1

        # return j  # new length after removals
        

        # for i in range(0, N-1): # (N-1) * (N-2)/2 --> N^2 
        #     if nums[i] == val:
        #         j = i+1
        #         while j<N-1: 
        #             if nums[j] != val:
        #                 break
        #             j+=1
        #         nums[i], nums[j] = nums[j], nums[i]
        # k = 0
        # for i in range(0, N): # O(N)
        #     if nums[i]==val:
        #         break
        #     k+=1
        
        # return k

    """
    nums --> List
    val --> Int
    k --> The elements in nums which are not equal to val
    Return k such that nums with first k elements that are not equal to val.

     nums = [3,2,2,3], val = 3

     return k

    Loop through the list:
        if we find val:
            j=i+1
            while j<len(nums)-1
                if nums[j]!=val
                    break
                j+=1
            swap with j.
    Loop through the list:
        increment k until we hit val
    """