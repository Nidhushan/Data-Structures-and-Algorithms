class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        max_len = 0
        mask = 0

        for right, x in enumerate(nums):
            while (mask & x) != 0:
                mask ^= nums[left]
                left+=1
            mask |= x
            max_len = max(max_len, right-left+1)
        
        return max_len
            

        """
        Question:
        nums - List[int]
        return longest nice subarray

        Solution:
        TwoPointer:
        use bitwise or to include the bits,
        check for bitwise and remove left pointer
        """