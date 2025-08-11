class Solution:
    def sortString(self, s: str) -> str:
        N = len(s)
        letters = sorted(set(s))
        di = Counter(s)
        res = []
        while sum(di.values())>0:    
            for i in letters:
                if di[i]>0:
                    res.append(i)
                    di[i]-=1
            for i in letters[::-1]:
                if di[i]>0:
                    res.append(i)
                    di[i] -= 1

        return "".join(res)

        """
        Question:
        s - string
        follow the rules and return resulting string

        Solution:
        create a frequency counter of s
        create a letters list with sorted letters of s that are unique
        go smallest and largest until you exhaust the chars.
        """