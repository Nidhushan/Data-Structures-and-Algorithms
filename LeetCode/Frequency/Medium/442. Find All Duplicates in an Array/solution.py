class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # res = []

        # for i in nums:
        #     idx = abs(i)-1
        #     if nums[idx]<0:
        #         res.append(abs(i))
        #     else:
        #         nums[idx] = -nums[idx]
        # # (Optional) restore: for i in range(len(nums)): nums[i] = abs(nums[i])
        # return res

        n = len(nums)
        i = 0
        while i < n:
            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        res = []
        for i, v in enumerate(nums):
            if v != i + 1:      # out of place → duplicate value v
                res.append(v)
        return res

        """
        Question:
        nums: List[int] - list of numbers
        return: List[int] - list of numbers that appears twice

        Solution:
        #1 sign negation method
        #2 Cyclic Placement
        """