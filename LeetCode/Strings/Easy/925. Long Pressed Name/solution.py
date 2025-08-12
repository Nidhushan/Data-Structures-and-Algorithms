class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        M = len(typed)
        while j<M:
            if i<len(name) and name[i] == typed[j]:
                i+=1; j+=1
            elif j>0 and typed[j] == typed[j-1]:
                j+=1
            else:
                return False
        
        return i==len(name)

        # j = 0
        # N = len(name)
        # prev = name[0]
        # for i in typed:
        #     if j<N and i == name[j]:
        #         prev = i
        #         j+=1
        #         continue
        #     elif i == prev:
        #         continue
        #     else:
        #         return False
        
        # return j==N


        """
        Question:
        name - String
         Return True if it is possible that it was your friends name, 
         with some characters (possibly none) being long pressed.
        
        Solution:
        Loop through the typed
        check name char with typed and prev name char
        """