class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s)<2:
            return ""
        chars = set(s)
        for i, ch in enumerate(s):
            if ch.swapcase() not in chars:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                return left if len(left)>=len(right) else right
        return s

        """
        Question:
        s - String
        find the longest nice string and return it

        Solution:
        Sliding Window? But how would I go about checking it.
        I think hash table works, in a way.
        """