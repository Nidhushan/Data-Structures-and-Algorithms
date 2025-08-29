class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # time.sort()
        if totalTrips<=1:
            return min(time)

        def is_ok(t: int) -> bool:
            trips = 0
            for i in time:
                trips+=t//i
                if trips>=totalTrips:
                    return True
            return False


        l, r = 1, min(time)*totalTrips
        
        while l<r:
            mid = l + (r-l)//2
            if is_ok(mid):
                r = mid
            else:
                l = mid+1
        return l

        """
        Question:
        time: List[int]: time taken by ith bus to complete one trip
        totalTrips: int: total no of trips to complete
        return: int: min time in which all trips can be completed

        Solution:
        Binary search in time
        """
