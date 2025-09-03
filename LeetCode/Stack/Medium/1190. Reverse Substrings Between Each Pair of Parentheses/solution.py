class Solution:
    def reverseParentheses(self, s: str) -> str:
        stck = []
        for i in s:
            if i!=")":
                stck.append(i)
                continue

            reverse = []
            while stck and stck[-1]!="(":
                reverse.append(stck.pop())
            if stck and stck[-1]=="(":
                stck.pop()
            else:
                return "".join(stck)

            stck.extend(reverse)
        
        return "".join(stck)



        """
        Question:
        s: str - lowercase english letters with brackets
        return: str - after reversing everything in each pair of brackets

        Solution:
        push in stack, when you see a ) reverse until (
        """