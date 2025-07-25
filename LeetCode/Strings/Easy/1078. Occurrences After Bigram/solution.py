class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        li = text.split()
        res = []
        for i in range(len(li)-2):
            if li[i] == first:
                if li[i+1] == second:
                    res.append(li[i+2])
        
        return res

        """
        Question:
        String - text, first, second

        if there is first in text and second immediately after first, add third word to the result.

        split the text into words
        for word in list of words:
            if word is first:
                if word+1 is second:
                    add word+2 to res
        
        return res
        """