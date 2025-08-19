class Solution:
    def partitionString(self, s: str) -> int:
        # temp = ""
        # substrings = []
        # N = len(s)
        # for i in range(N):
        #     if s[i] not in temp:
        #         temp+=s[i]
        #         if i == N-1:
        #             substrings.append(temp)
        #     else:
        #         substrings.append(temp)
        #         temp = s[i]
        #         if i == N-1:
        #             substrings.append(s[i])

        #     # print(temp, substrings)

        # return len(substrings)

        cnt = 1
        seen = set()

        for char in s:
            if char in seen:
                cnt += 1
                seen = set()
            seen.add(char)

        return cnt

        """
        Question:
        s - String
        find min no. of substrings in s, that have unique letters.

        Solution:
        Lets try group until you find a duplicate.
        """