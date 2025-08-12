class Solution:
    def checkString(self, s: str) -> bool:
        checkStr = 'a'
        for i in s:
            if i == 'b':
                checkStr = 'b'
            if checkStr != i:
                return False
        
        return True

        # return "ba" not in s

        """
        Question:
        s - String
        Check if all A's are before B's
        return True if satisfies

        Solution:
        Loop through s;
        check for a's till you hit a b
        then check for b's
        return false if not satisfies
        else return true

        """