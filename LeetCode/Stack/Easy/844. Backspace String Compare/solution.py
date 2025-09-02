class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def updStr(s: str) -> list:
            st = []
            for i in s:
                if i=="#":
                    if st:
                        st.pop()
                else:
                    st.append(i)
            return st
        
        return updStr(s) == updStr(t)


        """
        Question:
        s: str - string with # indicating backspace
        t: str - same as s
        return: bool - if s and t are equal after the backspaces

        Solution:
        push both into stacks(applying backspace) and check if they are equal

        """