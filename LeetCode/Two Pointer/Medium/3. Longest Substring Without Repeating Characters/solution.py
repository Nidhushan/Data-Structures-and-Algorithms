class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        left = 0
        best = 0

        for right, ch in enumerate(s):
            if ch in last and last[ch]>=left:
                left = last[ch]+1
            last[ch] = right
            best = max(best, right-left+1)
        return best

        
        # left = 0
        # max_len = 0
        # di = defaultdict(int)

        # for right, ch in enumerate(s):
        #     di[ch] += 1
        #     while di[ch] > 1:
        #         di[s[left]] -= 1
        #         left += 1
        #     max_len = max(max_len, right - left + 1)

        # return max_len



        """
        Question:
        s - String
        find longest unique charactered substring

        Solution:
        Have two pointers, and a hash table
        update the hash table while looping through 
        keep track of max(length)
        """