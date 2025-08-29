class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        r = sum(candies)//k
        if r==0: return 0

        def is_ok(cndy: int) -> bool:
            cnt = 0
            for i in candies:
                cnt += i//cndy
                if cnt>=k:
                    return True
            return False

        l = 1
        while l<r:
            mid = l + (r-l+1)//2
            if is_ok(mid):
                l = mid
            else:
                r = mid-1
        return l

        """
        Question:
        candies: List[int]: no of a type of candy
        k: int: no of children
        return: max. no. of candies you can allocate to all 3 children equally

        Solution:
        Binary search(upper bound) on no. of candies
        """