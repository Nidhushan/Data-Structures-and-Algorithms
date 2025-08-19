class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u']
        vowel_in_s = []
        N = len(s)
        for i in s:
            if i.lower() in vowels:
                vowel_in_s.append(i)
        
        vowel_in_s.sort()
        s = list(s)
        j = 0
        for i in range(N):
            if s[i].lower() in vowels:
                s[i] = vowel_in_s[j]
                j+=1

        return "".join(s)

        """
        Question:
        s - String
        sort the vowels in the string leaving consonants in place.

        Solution:
        create a list of vowels
        get all vowels from s
        sort the vowels
        loop through s and replace with sorted vowels
        """