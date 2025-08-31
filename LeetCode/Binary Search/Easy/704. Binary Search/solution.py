class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            mid = l+(r-l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1
        return -1


        """
        Question:
        nums: List[int]: list of numbers
        target: int: target to find in nums
        return: int: index of target if available else -1
        Constraint: do this in O(logn) time complexity

        Solution:
        Binary Search for target
        """