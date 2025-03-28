class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        di = {}

        for i, v in enumerate(nums):
            if v in di and i-di[v]<=k:
                return True
            di[v] = i
        return False


        # seen = set()

        # for i in range(len(nums)):
        #     if nums[i] in seen:
        #         return True
        #     else:
        #         seen.add(nums[i])
            
        #     if len(seen)>k:
        #         seen.remove(nums[i-k])
        # return False