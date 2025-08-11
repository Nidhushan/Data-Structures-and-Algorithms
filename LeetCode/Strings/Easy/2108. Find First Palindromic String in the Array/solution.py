class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
            
        return ""

        """
        Question:
        words - List of words
        return first word that is a palindrome

        Solution:
        Loop through the words
        return if palindrome
        """