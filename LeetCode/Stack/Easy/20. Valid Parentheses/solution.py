class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2:
            return False
        
        bstack = []
        hashmap = {']': '[', '}': '{', ')': '('}

        for ch in s:
            if ch in hashmap:
                if not bstack or bstack[-1] != hashmap[ch]:
                    return False
                bstack.pop()
            else:
                bstack.append(ch)
        
        return not bstack

        

        # stck = []

        # for i in s:
        #     if stck and ((stck[-1]=="(" and i==")") or (stck[-1]=="[" and i=="]") or (stck[-1]=="{" and i=="}")):
        #         stck.pop()
        #     else:
        #         stck.append(i)
        # return not stck

        """
        Question:
        s: str - contains brackets (, ), [, ], {, }
        return: bool - if s is valid sequence of brackets

        Solution:
        use a hashmap to store the brackets
        use a stack to push and pop the brackets,
        return true if stack empty

        #2 stck without hashmap, just using checks
        """
