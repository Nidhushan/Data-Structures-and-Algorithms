class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = "".join([char for char in s.lower() if char.isalnum()])
        return res == res[::-1]
        
        # res = ""
        # s = s.lower()
        # for i in s:
        #     if i.isalnum():
        #         res += i
            
        # return res == res[::-1]

            

        """
        Question:
        s - string
        return if alpha chars in s is a palindrome

        Solution:
        new list containing all alpha chars in lower case
        return true if palindrome
        """