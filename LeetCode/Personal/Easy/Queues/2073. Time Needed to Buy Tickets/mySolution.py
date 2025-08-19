class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        time = 0

        for i in range(len(tickets)):
            if i<=k:
                time += min(tickets[i], tickets[k])
            else:
                time += min(tickets[i], tickets[k]-1)
        return time
        
        # Brute Force method
        # time = 0

        # while tickets[k]>0:
        #     for i in range(len(tickets)):
        #         if tickets[i]>0:
        #             time+=1
        #             tickets[i]-=1
        #         if i==k and tickets[i]==0:
        #             return time
        