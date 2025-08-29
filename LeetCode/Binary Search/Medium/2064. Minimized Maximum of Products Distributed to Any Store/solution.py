class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        
        def is_ok(x: int) -> bool:
            cnt = 0
            for i in quantities:
                cnt += (i + x - 1)//x
                if cnt>n:
                    return False
            return True
        
        total = sum(quantities)
        l = max(1, ceil(total / n))   # stronger lower bound than 1
        r = max(quantities)
        while l<r:
            mid = l+(r-l)//2
            if is_ok(mid):
                r = mid
            else:
                l = mid+1
        return l

        """
        Question:
        n: int: no of specialty retail stores.
        quantities: List[int]: no of products
        return: x int: min(max no. of products given to any store)

        Solution:
        binary search to find x
        """