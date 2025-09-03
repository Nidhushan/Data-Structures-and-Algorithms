class Solution:
    def firstUniqChar(self, s: str) -> int:
       

        # Slower in this level

        # freq = [0]*26
        # for i in s:
        #     freq[ord(i)-97] += 1
        
        freq = Counter(s)
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1

        """
        Question:
        s: str - string of lowercase english letters
        return: int: index of first non repeating letter

        Solution:
        create a freq hashmap
        find first letter with freq = 1
        """