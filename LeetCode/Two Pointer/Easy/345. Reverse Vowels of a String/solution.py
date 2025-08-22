class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s = list(s)

        i, j = 0, len(s)-1
        while i<j:
            while i<j and s[i] not in vowels:
                i+=1

            while i<j and s[j] not in vowels:
                j-=1

            s[i], s[j] = s[j], s[i]

            i+=1
            j-=1

        return "".join(s)


        """
        Question:
        s - string
        reverse the vowels in the string and return it

        Solution:
        have two pointers, 
        find the vowels in opposite ends and swap them
        """