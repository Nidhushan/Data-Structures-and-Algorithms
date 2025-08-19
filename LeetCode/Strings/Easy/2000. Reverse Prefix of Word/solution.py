class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            N = word.index(ch)
        else:
            return word
        return word[:N+1][::-1] + word[N+1:]

        """
        Question:
        word - String
        ch - String of length 1
        return reversed segment from index 0 to index(ch)

        Solution:
        use index to find index of ch
        return reversed segment with rest

        """