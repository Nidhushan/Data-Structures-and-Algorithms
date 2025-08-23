class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums = sorted(nums)
        N = len(nums)
        i = 0
        marked = 0

        for j in range(N-N//2, N):
            if nums[i]*2 <= nums[j]:
                marked+=2
                i+=1
        return marked

        """
        Question:
        nums - List[int]
        mark the indices according to the rule and return max possible number of marks

        Solution:
        [3,5,2,4] -> [5, 4, 3, 2]

        sort the array, in reverse
        two pointer, one at the beginning, other moves till value is half
        increments marked by 2
        """