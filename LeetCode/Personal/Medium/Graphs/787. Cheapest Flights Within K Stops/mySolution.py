class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')]*n
        prices[src] = 0

        for i in range(k+1):
            tmpPrices = prices.copy()

            for from_node, to_node, cost in flights:

                if prices[from_node] == float('inf'):
                    continue
                
                if prices[from_node] + cost < tmpPrices[to_node]:
                    tmpPrices[to_node] = prices[from_node] + cost
                
            prices = tmpPrices
        
        if prices[dst] == float('inf'):
            return -1
        else:
            return prices[dst]
