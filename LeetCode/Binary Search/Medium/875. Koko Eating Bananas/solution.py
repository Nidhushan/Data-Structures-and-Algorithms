class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_ok(k: int) -> bool:
            hrs = 0
            for p in piles:
                hrs += (p+k-1)//k
                if hrs>h:
                    return False
            return True
            
        l, r = 1, max(piles)

        while l<r:
            mid = l+(r-l)//2

            if is_ok(mid):
                r = mid
            else:
                l = mid+1
        return l
        


        """
        Question:
        piles: List[int]: no of bananas in each pile
        h: int: hours left to eat
        return: int: k - no of bananas eaten from a pile per hour

        Solution:
        binary search in max(piles)
        return min k
        """
