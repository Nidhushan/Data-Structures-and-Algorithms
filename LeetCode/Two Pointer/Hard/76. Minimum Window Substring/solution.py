class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""
        freq = Counter(t)
        letters = len(freq)
        N = len(s)
        left = 0
        ans_left = ans_right = 0
        min_len = float("inf")

        for right, x in enumerate(s):
            if x in freq:
                freq[x] -= 1
                if freq[x] == 0:
                    letters-=1
            while letters == 0:

                if min_len > right-left+1:
                    min_len = right-left+1
                    ans_left, ans_right = left, right

                if s[left] in freq:
                    freq[s[left]] += 1
                    if freq[s[left]] > 0:
                        letters+=1
                left+=1
                
        return "" if min_len == float("inf") else s[ans_left:ans_right+1]


        """
        Question:
        s, t - String
        return the minimum window substring of s such that every character in t (including duplicates) is included in the window

        Solution - Sliding Window:
        create a hashmap of t
        check for all t in the current window
        if not increment left till you meet a letter in t
        retrun smallest window
        """ 