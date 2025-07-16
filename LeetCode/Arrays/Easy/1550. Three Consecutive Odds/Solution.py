class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # odd_count = 0
        for i in range(2,len(arr)):
            if arr[i]%2!=0 and arr[i-1]%2!=0 and arr[i-2]%2!=0:
                return True
            
        return False


        # if i%2!=0:
            #     odd_count+=1
            #     if odd_count == 3:
            #         return True
            # else:
            #     odd_count = 0