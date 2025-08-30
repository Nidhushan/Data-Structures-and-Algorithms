class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def is_ok(pen: int) -> bool:
            cnt = 0
            for i in nums:
                if i>pen:
                    cnt+= (i-1)//pen
                    if cnt>maxOperations:
                        return False
            return True
        
        l, r = 1, max(nums)

        while l<r:
            mid = l+(r-l)//2
            print(mid)
            if is_ok(mid):
                r = mid
            else:
                l = mid+1
        return l



        """
        Question:
        nums: List[int]: number of balls
        maxOperations: int: max no of operations
        return: int: min penalty(max number of balls)

        Solution:
        Binary search on penalty
        """