class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # low, high = 1, len(nums) - 1
        # while low < high:
        #     mid = (low + high) // 2
        #     cnt = sum(x <= mid for x in nums)
        #     if cnt > mid:
        #         high = mid
        #     else:
        #         low = mid + 1
        # return low

        # 2
        # phase 1: find intersection
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # phase 2: find cycle entrance (duplicate)
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


        """
        Question:
        nums: List[int] - list of numbers of len n+1
        return: int - number that repeats
        Constraints - each i in nums will be in [1,n] inclusive
        solve the problem withoud modifying the array nums and in constant extra space

        Solution:
        #1 Binary Search - O(nlogn) time and constant space
        #2 Floyds Tortoise and Hare - O(n) time and constant space
        """