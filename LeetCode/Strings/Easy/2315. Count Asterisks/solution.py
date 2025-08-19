class Solution:
    def countAsterisks(self, s: str) -> int:
        s = s.split('|')
        sum = 0
        for i in range(0, len(s), 2):
            sum += s[i].count('*')
        
        return sum

        
        # lineCnt = 0
        # starCnt = 0
        # for i in s:
        #     if lineCnt%2 == 0 and i=='*':
        #         starCnt += 1
        #     if i == '|':
        #         lineCnt += 1
        # return starCnt

        """
        Question:
        s - String
        return no of * excluding the ones in between pairs

        Solution:
        if line count is even(starting from 0) count
        else dont count
        return count
        """