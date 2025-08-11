class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for i in sentences:
            max_words = max(max_words, len(i.split()))
        
        return max_words

        """
        Question:
        sentences - List of strings
        Find which sentence has most words.
        return max no of words in a sentence

        Solution:
        take each sentence and find len. Return max
        """