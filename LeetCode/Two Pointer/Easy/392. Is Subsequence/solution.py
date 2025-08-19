class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0

        for right in range(len(t)):
            if left>=len(s):
                return True
            if s[left] == t[right]:
                left+=1
            
        if left == len(s):
            return True
        else:
            return False


        """
        s, t --> Strings
        return true if s is a subsequence of t

        Input: s = "abc", t = "ahbgdc"
        Output: true    
        
        Solution:
        left = 0
        loop right through t:
            if s[left] == t[right]:
                left+=1
            
        if left == len(s):
            return True
        else:
            return false
            
        """