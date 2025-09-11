class Solution:
    def fib_fast_doubling_iter(self, n: int) -> tuple[int, int]:
        a, b = 0, 1   # F(0), F(1)
        # process bits of n from most significant to least
        for bit in bin(n)[2:]:
            c = a * ((b << 1) - a)   # F(2k)
            d = a*a + b*b            # F(2k+1)
            if bit == "0":
                a, b = c, d
            else:
                a, b = d, c + d
        return a, b   # returns (F(n), F(n+1))

    def climbStairs(self, n: int) -> int:
        if n<=1: return 1
        prev2, prev1 = 1, 1

        for i in range(2, n+1):
            prev2, prev1 = prev1, prev1+prev2
        return prev1
        # dp = [0] * (n+1)
        # dp[0] = dp[1] = 1

        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        
        # return dp[n]

        # best time and space: O(logn), O(1)
        # return self.fib_fast_doubling_iter(n + 1)[0]


        """
        Question:
        n: int - no of steps to climb to the top.
        return: int - no of ways you can climb those n steps

        Solution:
        Recursive/iterative DP - Fibonacci similar
        """