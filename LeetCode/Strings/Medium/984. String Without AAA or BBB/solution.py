class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        res = []
        while a > 0 or b > 0:
            if a > b:
                if a >= 2:
                    res.extend(['a', 'a'])
                    a -= 2
                else:
                    res.append('a')
                    a -= 1
                if b > 0:
                    res.append('b')
                    b -= 1
            elif b > a:
                if b >= 2:
                    res.extend(['b', 'b'])
                    b -= 2
                else:
                    res.append('b')
                    b -= 1
                if a > 0:
                    res.append('a')
                    a -= 1
            else:  # a == b
                res.append('a')
                res.append('b')
                a -= 1
                b -= 1
        return ''.join(res)


        # larger = "a" if a >= b else "b"
        # smaller = "b" if larger == "a" else "a"
        # larger_num = max(a, b)
        # smaller_num = min(a, b)
        # res = []

        # while larger_num > smaller_num and larger_num > 0 and smaller_num > 0:
        #     res.append(larger)
        #     res.append(larger)
        #     res.append(smaller)
        #     larger_num -= 2
        #     smaller_num -= 1

        # while larger_num > 0 and smaller_num > 0:
        #     res.append(larger)
        #     res.append(smaller)
        #     larger_num -= 1
        #     smaller_num -= 1

        # while larger_num > 0:
        #     res.append(larger)
        #     larger_num -= 1

        # while smaller_num > 0:
        #     res.append(smaller)
        #     smaller_num -= 1

        # return ''.join(res)

    """
    Question:
    Int - a, b
    we need to make a string s such that we have 'a' number of a's and 'b' number of b's
    Condition:
    There should be no 3 a's or b's in a row(like 'aaa' or 'bbb') in s
    
    
    find which is larger, a or b
    add 2 larger num and 1 smaller num until the numbers become equal and then alternate.

    """