class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        N = len(s)-1
        left = 0
        while left<=N:
            s[left], s[N] = s[N], s[left]
            left += 1
            N -= 1
        
        
        # # print(len(s))
        # N = len(s)
        # x = (N-1)//2

        # for i in range(x+1):
        #     # print(i)
        #     s[i], s[-i-1] = s[-i-1], s[i]
        

        """
        s --> list of characters
        reverse s in place
        Use only O(1) extra memory

        Solution:
        n = len(s)

        x = (n-1)//2

        for i upto x:
            swap with -i of list
        
        Two Pointer:
        N = len(s)
        left = 0
        right = N-1
        while left<right:
            swap left and right
        
        """
        