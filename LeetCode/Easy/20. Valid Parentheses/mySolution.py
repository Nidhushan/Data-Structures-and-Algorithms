class Solution:
    def isValid(self, s: str) -> bool:
        bstack = []
        hashmap = {']': '[', '}': '{', ')': '('}

        for ch in s:
            if bstack and (ch in hashmap and bstack[-1] == hashmap[ch]):
                bstack.pop()
            else:
                bstack.append(ch)
        
        return not bstack
