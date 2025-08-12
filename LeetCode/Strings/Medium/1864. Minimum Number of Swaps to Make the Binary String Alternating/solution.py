class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        ones = s.count('1')
        zeros = n - ones
        if abs(ones - zeros) > 1:
            return -1

        def mismatches(start_char: str) -> int:
            expect = start_char
            mis = 0
            for ch in s:
                if ch != expect:
                    mis += 1
                expect = '1' if expect == '0' else '0'
            return mis

        if ones > zeros:          # must start with '1'
            return mismatches('1') // 2
        elif zeros > ones:        # must start with '0'
            return mismatches('0') // 2
        else:                     # both patterns possible
            return min(mismatches('0'), mismatches('1')) // 2

        """
        Question:
        s - Binary string
        return min no of swaps to make it alternating

        Solution:
        if the previous digit is same as current swap with next alternate - Failed
        count zeroes and ones. 
        define mismatches function
            return no of mismatches.
        call function based on condition
        """