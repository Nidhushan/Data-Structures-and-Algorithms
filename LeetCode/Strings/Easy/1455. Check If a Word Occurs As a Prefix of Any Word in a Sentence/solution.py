class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        sw_len = len(searchWord)
        for i in range(len(words)):
            N = len(words[i])
            if N>=sw_len:
                if words[i][:sw_len] == searchWord:
                    return i+1
            
        return -1


        """
        question:
        sentence - string
        searchWord - string

        check if searchWord is a prefix of any word in sentence.
        return min index

        solution:
        split sentence into words
        check if searchWord is prefix of any word
        return index

        """