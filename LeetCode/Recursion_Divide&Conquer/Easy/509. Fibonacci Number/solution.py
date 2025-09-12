class Solution:
    def fib(self, n: int) -> int:
        # Iterative:
        if n==0:
          return 0
        prev2, prev1 = 1, 1

        for i in range(2, n):
            prev2, prev1 = prev1, prev2+prev1
        
        return prev1

        # recursive:
        # if n==0 or n==1:
        #     return n
        
        # return self.fib(n-1) + self.fib(n-2)


        """
        Question:
        n: int - number
        return: int - fibonacci of number

        Solution:
        iterative:
        add past two numbers to current
        Recursive(preferably tail for other languages):
        recursively call the function after base case
        """