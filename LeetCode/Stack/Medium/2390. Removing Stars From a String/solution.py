class Solution:
    def removeStars(self, s: str) -> str:
        stck = []

        for i in s:
            if i=='*':
                stck.pop()
            else:
                stck.append(i)
        return "".join(stck)
            



        """
        Question:
        s: string - contains *'s
        return: string - removing stars and its left character

        Solution:
        push them in a stack and pop for each star
        """
        