class Solution:
    def removeDuplicates(self, s: str) -> str:
        stck = []

        for i in s:
            if stck and i == stck[-1]:
                stck.pop()
            else:
                stck.append(i)
        return "".join(stck)

        """
        Question:
        s: string - lowercase english letters
        return: string(s) - after repeatedly removing duplicates.

        Solution:
        Use a stack and pop all duplicates
        """