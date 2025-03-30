class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, end):
            if start == end:
                res.append(nums[:])
                return

            for i in range(start, end):
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(start+1, end)
                nums[i], nums[start] = nums[start], nums[i]

        backtrack(0, len(nums))
        return res