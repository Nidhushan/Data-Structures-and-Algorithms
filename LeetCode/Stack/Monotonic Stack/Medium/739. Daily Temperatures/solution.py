class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # N = len(temperatures)
        # stck = []
        # res = [0] * N

        # for i in range(N):
        #     while stck and temperatures[stck[-1]]<temperatures[i]:
        #         res[stck[-1]] = i-stck[-1]
        #         stck.pop()
        #     stck.append(i)
        
        # return res

        # Slightly more efficient:
        n = len(temperatures)
        res = [0] * n
        st = []
        arr = temperatures  # local alias

        for i, t in enumerate(arr):
            while st and arr[st[-1]] < t:
                j = st.pop()
                res[j] = i - j
            st.append(i)
        return res
        """
        Question:
        temperatures: List[int] - list of temperatures on each day
        return: List[int] - the next day its warmer than that current day

        Solution:
        Use a monotonically decreasing stack to track
        """