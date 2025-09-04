class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # N = len(nums)
        # res = [-1] * N
        # stck = []

        # for i in range(2 * N):
        #     cur = nums[i%N]
        #     while stck and nums[stck[-1]]<cur:
        #         res[stck.pop()] = cur
        #     if i<N:
        #         stck.append(i)

        # return res
        
        # Slight variation
        n = len(nums)
        res = [-1] * n
        st = []
        arr = nums  # local alias

        for i in range(2 * n):
            cur = arr[i - n] if i >= n else arr[i]
            while st and arr[st[-1]] < cur:
                res[st.pop()] = cur
            if i < n:           # push only on first pass
                st.append(i)
        return res


        """
        Question:
        nums: List[int]. - list of numbers
        return: List[int] - list of numbers next greater than that index

        Solution:
        Make a monotonically decreasing stack with a condition to loop twice to imitate looping around
        """