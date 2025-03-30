class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch not in "+*-/":
                stack.append(int(ch))
            else:
                x, y = stack.pop(), stack.pop()
                if ch=='+':
                    stack.append(y+x)
                elif ch=='-':
                    stack.append(y-x)
                elif ch=='*':
                    stack.append(y*x)
                elif ch=='/':
                    stack.append(int(float(y)/x))
        return stack.pop()