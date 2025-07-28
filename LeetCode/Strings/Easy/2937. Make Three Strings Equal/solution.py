class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        
        lcp = 0
        min_lcp = min(len(s1), len(s2), len(s3))

        for i in range(min_lcp):
            if s1[i] == s2[i] == s3[i]:
                lcp +=1
            else:
                break
            
        if lcp == 0:
            return -1
        
        return (len(s1) - lcp) + (len(s2) - lcp) + (len(s3) - lcp)
        
        # count = 0
        # while len(s1)>0 and len(s2)>0 and len(s3)>0:
        #     if s1 == s2 and s2 == s3:
        #         return count
            
        #     if s1 > s2 and s1 > s3:
        #         s1 = s1[:-1]
        #         print("S1", s1)
        #     elif s2 >= s1 and s2 >= s3:
        #         s2 = s2[:-1]
        #         print("s2", s2)
        #     else:
        #         s3 = s3[:-1]
        #         print("s3", s3)
            
        #     count+=1
            
        # return -1

        """
        Question:
        Given s1, s2, s3 --> String
        One Operation: delete the rightmost character from one of the strings
        Return min no. of deletions to make the string equal
        return -1 if not possible to equate them

        loop through until one of the strings reaches len 0
        if strings are equal return count
        remove a letter from greatest string
        return -1 if not possible
        """