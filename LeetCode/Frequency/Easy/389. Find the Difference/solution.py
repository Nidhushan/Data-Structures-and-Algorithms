class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # freqT = Counter(t)
        # freqS = Counter(s)

        # for i in freqT:
        #     if i not in freqS:
        #         return i
        #     if freqT[i]>freqS[i]:
        #         return i


        # 
        # return list((Counter(t) - Counter(s)).keys())[0]


        # 
        # xor = 0
        # for ch in s + t:
        #     xor ^= ord(ch)
        # return chr(xor)


        # 
        return chr(sum(map(ord, t)) - sum(map(ord, s)))


        """
        Question:
        s: str - string of lowercase english letters
        t: str - same as s
        return: str - letter that has been added to t

        Solution:
        find freq of all and return the letter which has more freq in t
        Using XOR
        using sum of ords
        """