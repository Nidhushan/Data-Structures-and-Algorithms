class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l<r:
            mid = l+(r-l)//2
            if mid%2 == 1:
                mid -= 1
            if nums[mid] == nums[mid+1]:
                l = mid+2
            else:
                r = mid
        return nums[l]

        """
        Question:
        nums: List[int] - list of sorted numbers with all elements coming twice except one integer.
        return: int - number that comes only once
        Constraint:
        do it in O(log n) time and O(1) space

        Solution:
        You can use freq using a hashmap to find this in O(n)
        but since they are asking O(log n) we will be using binary search
        """