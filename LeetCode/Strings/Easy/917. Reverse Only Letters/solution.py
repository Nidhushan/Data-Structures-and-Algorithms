class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        temp = []
        for i in s:
            if i.isalpha():
                temp.append(i)
        
        temp = temp[::-1]
        
        res = ""
        j = 0
        for i in s:
            if i.isalpha():
                res += temp[j]
                j+=1
            else:
                res += i
        
        return res

        """
        Question:
        s - string
        reverse all the letters alone in s

        Solution:
        Create a list of all alphabets in s
        reverse this list
        put it back in s
        """