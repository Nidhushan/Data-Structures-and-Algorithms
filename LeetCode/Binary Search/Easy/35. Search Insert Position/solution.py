class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # inclusive interval [l, r]
        l, r = 0, len(nums)-1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1
        return l

        
        # half-open interval [l, r)
        
        # l, r = 0, len(nums)

        # while l<r:
        #     mid = l+(r-l)//2
        #     if nums[mid]<target:
        #         l = mid+1
        #     else:
        #         r = mid
        # return l


        """
        Question:
        nums - List[int] - sorted array
        target - int
        return: int - index where target is or should be inserted

        Solution:
        Binary search and return index
        """