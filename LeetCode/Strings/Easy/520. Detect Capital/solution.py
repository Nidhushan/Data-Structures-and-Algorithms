class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        
        if ord(word[0])>=65 and ord(word[0])<=90:
            if ord(word[1])>=65 and ord(word[1])<=90:
                for i in word[2:]:
                    if ord(i)>=97:
                        return False
            else:
                for i in word[2:]:
                    if ord(i)<97:
                        return False
            
        else:
            for i in word[1:]:
                    if ord(i)<97:
                        return False
        
        return True

        # if word.islower() or word.isupper() : return True
        # if word[0].isupper() and word[1:].islower() : return True
        # return False

        """
        Question:
        Rules: 
            All letters in this word are capitals, like "USA".
            All letters in this word are not capitals, like "leetcode".
            Only the first letter in this word is capital, like "Google".
        return true if rules are followed and not broken.


        Solution:
        Check first letter
            Capital:
                check all caps
                (or) check all small after
            Small:
                All should be small letters.
        """