class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        res = [""]

        for i in range(len(s)):
            temp = []
            
            if s[i].isalpha():
                for r in res:
                    temp.append(r+s[i].upper())
                    temp.append(r+s[i].lower())
            else:
                for r in res:
                    temp.append(r+s[i])
            res = temp
        
        return res
        
        
        # worse space complexity (N + 2^N) solution - Backtracking

        # res = []

        # def backtrack(sub="", i=0):

        #     if len(sub) == len(s):
        #         res.append(sub)
        #         return
            
        #     if s[i].isalpha():
        #         backtrack(sub+s[i].swapcase(), i+1)
        #     backtrack(sub+s[i], i+1)
        
        # backtrack()

        # return res