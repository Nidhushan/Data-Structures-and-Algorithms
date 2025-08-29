class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        if cars==1:
            return min(ranks)
        N = len(ranks)
        def is_ok(time: int) -> int:
            cnt = 0
            for r in ranks:
                cnt += isqrt(time//r)
                if cnt>=cars:
                    return True
            return False
        

        
        ranks.sort()
        l, r = ranks[0], ranks[0]*cars*cars
        while l<r:
            mid = l + (r-l)//2
            if is_ok(mid):
                r = mid
            else:
                l = mid+1
        return l


        """
        Question:
        ranks: List[int]: rank of each mechanic
        cars: no. of cars to repair
        return: int: time taken to repair all cars
        Time taken for a mechanic to repair a car = rank * n * n

        Solution:
        sort
        find time = r*cars^2
        cars^2 = time/r
        cars = sqrt(time/r)
        do binary search in that range
        return minimum time taken
        """