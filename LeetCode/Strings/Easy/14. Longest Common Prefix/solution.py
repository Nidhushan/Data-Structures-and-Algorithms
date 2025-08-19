class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        min_len = len(strs[0])
        for i in strs:
            min_len = min(min_len, len(i))
        # print(min_len)

        for i in range(min_len):
            for j in range(0, len(strs)-1):
                if strs[j][i]!=strs[j+1][i]:
                    # print(strs[j][i], strs[j-1][i])
                    return res
            res+=strs[0][i]
        
        return res

        """
        Question:
        strs --> list of strings
        return longest common prefix

        find the smallest string(which is the largest possible LCP)
        go through each word and check for inconsistency in their letters.
        if inconsistent, return res
        if no inconsistency, add the letter to res
        
        """