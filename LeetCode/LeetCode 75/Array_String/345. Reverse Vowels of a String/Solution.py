# Brute Force Method

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        strVowels = []
        for i in s:
            if i in vowels:
                strVowels.append(i)
            
        # strVowels = strVowels[::-1]
        s = list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = strVowels.pop()
        
        return ''.join(s)
    
# Two Pointer:

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