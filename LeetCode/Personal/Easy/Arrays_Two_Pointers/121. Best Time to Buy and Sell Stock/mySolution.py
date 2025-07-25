# Better runtime solution:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r!=len(prices):

            if prices[l] <= prices[r]:
                maxP = max(prices[r]-prices[l], maxP)
            else:
                l = r
            r+=1
        return maxP


# Good Memory Solution:
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         maxp=0
#         minp=1000000
#         for i in range(len(prices)):
#             if prices[i]<minp:
#                 minp=prices[i]
#             if prices[i]-minp>maxp:
#                 maxp=prices[i]-minp
#         return maxp 