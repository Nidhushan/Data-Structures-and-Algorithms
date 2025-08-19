class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        r_cnt = 0

        for i in s:
            if i=='R':
                r_cnt+= 1
            else:
                r_cnt -= 1
            if r_cnt == 0:
                cnt+=1

        return cnt
        """
        Question:
        s - string
        balanced is equal no of L and R
        return max number of balanced substrings possible.

        Solution:
        Loop through s and each time L and R are equal increment count
        return count after looping
        """