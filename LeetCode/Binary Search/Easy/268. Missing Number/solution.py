class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Better sum method:
        
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
        
        # Set Method

        # s = set(nums)
        # n = len(nums)
        # for x in range(n + 1):
        #     if x not in s:
        #         return x


        # XOR Solution:

        # n = len(nums)
        # x = 0
        # # XOR all indices 0..n
        # for i in range(n + 1):
        #     x ^= i
        # # XOR all values in nums
        # for v in nums:
        #     x ^= v
        # return x
        

        # Binary Search

        # nums.sort()
        # l, r = 0, len(nums)
        # while l<r:
        #     mid = l + (r-l)//2
        #     if nums[mid]>mid:
        #         r = mid
        #     else:
        #         l = mid + 1
        # return l

        
        
        # return sum(range(len(nums)+1))-sum(nums)

        """
        Question:
        nums - List[int] - range [0,n]
        return: int - missing number in range

        Solution:
        - O(n log n): sort and then binary search for the first index i where nums[i] > i
        - O(n): use Gauss sum formula (n*(n+1)//2 - sum(nums))
        - O(n): use XOR trick to cancel all numbers with their indices
        - O(n): use a hash set and check which number in [0..n] is missing
        """