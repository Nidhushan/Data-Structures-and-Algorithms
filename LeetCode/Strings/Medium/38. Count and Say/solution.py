class Solution:
    def countAndSay(self, n: int) -> str:
        
        def rle(s):
            res = ""
            count = 1
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    count+=1
                else:
                    res += str(count) + str(s[i-1])
                    count = 1
                
            res += str(count) + str(s[-1])

            return res


        res = ""
        for i in range(1, n+1):
            if i == 1:
                res = "1"
            if i>1:
                res = rle(res)
            
        return res
            
        """
        Question:
        Given n -> int
        find grouped consecutive digit counts

        Example:
        countAndSay(1) = "1"
        countAndSay(2) = RLE of "1" = "11"
        countAndSay(3) = RLE of "11" = "21"
        countAndSay(4) = RLE of "21" = "1211"

        rle:
            loop through the digits, increment count for same digits and add to res -> "count" + "digit"

        for each value of 1 to n:
            calculate rle and set to res
        """
