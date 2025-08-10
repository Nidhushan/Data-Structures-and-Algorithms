class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = {}
        for i in text:
            letters[i] = letters.get(i, 0) + 1
        
        req = ['b', 'a', 'n']
        max_bal = 0
        letters['l'] = letters.get('l', 0)
        letters['o'] = letters.get('o', 0)
        max_bal = min(letters['l']//2, letters['o']//2)
        for i in req:
            letters[i] = letters.get(i, 0)
            max_bal = min(max_bal, letters[i])
        
        return max_bal

        # text = Counter(text)
        # balloon = Counter("balloon")

        # maxballoons = float("inf")
        # for c in balloon:
        #     maxballoons = min(maxballoons, text[c] // balloon[c])
        # return maxballoons

        """
        Question:
        text - String
        find possible no of balloon you can make using the letters
        return no. of balloon possible
        Constraint:
        use each letter at most once

        Solution:
        put all letters in a dictionary
        take count of balon
        return number of balloon possible
        """