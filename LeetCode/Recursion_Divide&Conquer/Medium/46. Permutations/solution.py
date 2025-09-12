class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Use Yield for better memory management
        res = []
        def compute(nums):    
            def backtrack(start=0):
                if start == len(nums):
                    yield nums[:]           # snapshot
                    return
                for i in range(start, len(nums)):
                    nums[start], nums[i] = nums[i], nums[start]
                    yield from backtrack(start+1)
                    nums[start], nums[i] = nums[i], nums[start]   # backtrack
            return backtrack(0)

        # consume lazily:
        for p in compute(nums):
            res.append(p)
        return res
        
        
        # res = []

        # def recurse(start: int, end: int):
        #     if start == end:
        #         yield nums[:]
        #         return
            
        #     for i in range(start, end):
        #         nums[i], nums[start] = nums[start], nums[i]
        #         yield from recurse(start+1, end)
        #         nums[i], nums[start] = nums[start], nums[i]
            
        # recurse(0, len(nums))
        # return res
        
        """
        Question:
        nums: List[int] - list of numners
        return: List[List[int]] - list of list of all permutations possible of nums

        Solution:
        recursion on the list
        """