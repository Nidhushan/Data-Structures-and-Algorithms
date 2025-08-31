class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        N = len(heaters)

        # Two Pointer Solution:
        i = j = 0
        H = len(houses)
        Hradius = 0
        while i<H:
            while j+1 < N and abs(heaters[j+1]-houses[i])<=abs(heaters[j]-houses[i]):
                j+=1
            Hradius = max(Hradius, abs(heaters[j]-houses[i]))
            i+=1
        return Hradius
        



        # Binary Search Solution:

        # def is_ok(r: int) -> bool:
        #     j = 0
        #     for i in houses:
        #         while heaters[j]-r>i or heaters[j]+r<i:
        #             j+=1
        #             if j>=N:
        #                 return False
        #     return True

        # l, r = 0, max(houses[-1] - heaters[0], heaters[-1] - houses[0])
        # while l<r:
        #     mid = l+(r-l)//2
        #     if is_ok(mid):
        #         r = mid
        #     else:
        #         l = mid+1
        # return l

        """
        Question:
        houses: List[int]: position of houses in a horizontal line
        heaters: List[int]: position of heaters in a horizontal line
        return: int: min radius of heater needed for warming all houses.

        Solution:
        Binary search on radius
        """