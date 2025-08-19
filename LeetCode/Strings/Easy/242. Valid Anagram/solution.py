class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = [0] * 26
        base = ord('a')
        for i in s:
            freq[ord(i) - base] += 1
        for i in t:
            freq[ord(i) - base] -= 1
        
        for i in freq:
            if i<0:
                return False
        
        return True
        
        # return sorted(s) == sorted(t)
        
        # return Counter(s) == Counter(t)

        # s = Counter(s)
        # t = Counter(t)

        # for k, v in s.items():
        #     if t.get(k) and t[k] == v:
        #         continue
        #     return False
        
        # return True

        """
        Question:
        s, t - Strings
        return True if s is anagram of t

        Solution:
        take Counter for both s and t
        return s==t
        """