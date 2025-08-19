class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        max_count = 1
        s = list(s)
        for i in range(1, len(s)):
            # print(s[i])
            if s[i] == s[i-1]:
                count+=1
            else:
                count = 1
            
            max_count = max(max_count, count)
        return max_count

        """
        Question:
        s --> String
        power of s is the len of continuous unique characters.
        return power of s

        loop through the string
        if same letter as before increment count
        if diff letters, reset count
        update max count
        """