class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stck = []

        for i in operations:
            if i.isdigit():
                stck.append(int(i))
            elif i == "+":
                stck.append(stck[-1]+stck[-2])
            elif i == "D":
                stck.append(stck[-1]*2)
            elif i == "C":
                stck.pop()
            elif i[0] == "-" and len(i)>=2:
                stck.append(int(i[1:])*(-1))

        return sum(stck)


        """
        Question:
        operations: List[str]: list of operations
        return: int: sum of all scores

        Solution:
        use a stack to store the scores and apply the rules to them
        """