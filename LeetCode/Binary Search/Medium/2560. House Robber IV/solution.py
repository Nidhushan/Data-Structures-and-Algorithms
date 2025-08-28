class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        N = len(nums)
        def is_ok(amt: int) -> bool:
            i = 0
            cnt = 0
            while i<N:
                if amt>=nums[i]:
                    cnt+=1
                    if cnt>=k:
                        return True
                    i+=2
                else:
                    i+=1
            return False

        left, right = min(nums), max(nums)
        while left<right:
            mid = left + (right-left)//2
            if is_ok(mid):
                right = mid
            else:
                left = mid+1
        return left


        """
        Question:
        nums: List[int]: Money in each house
        k: int: no. of houses to rob

        Solution:
        find max and min of nums
        binary search within that length:
        check condition
        return min
        """