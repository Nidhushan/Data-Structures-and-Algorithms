class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        N = len(price)
        price.sort()
        def is_ok(amt: int) -> bool:
            if k<=1:
                return True
            cnt = 1
            last = price[0]
            for p in price[1:]:
                if p-last>=amt:
                    cnt+=1
                    last = p
                    if cnt>=k:
                        return True
            return False


        left, right = 0, price[-1]-price[0]
        while left<right:
            mid = left + (right-left)//2 + 1
            # mid = (left + right + 1)//2
            if is_ok(mid):
                left = mid
            else:
                right = mid - 1
        return left


        """
        Question:
        price: List[int]: prices of candies
        k: int: no of distinct candies 
        return: int: max tastiness of candies
        Tastiness: smallest absolute difference of the prices of any two candies

        Solution:
        sort price
        range = max(price)
        do binary search in range
        check condition, maximizing tastiness.
        return maximum tastiness
        """