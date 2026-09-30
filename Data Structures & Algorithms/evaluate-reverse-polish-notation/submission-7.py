class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: return int(tokens[0])
        stack = []
        for t in tokens:
            if t not in "+-*/": 
                stack.append(int(t))
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                ans = 0
                if t == "+": ans = a + b
                elif t == "-": ans = a - b
                elif t == "*": ans = a * b
                else: ans = int(a/b)
                stack.append(ans)
            
        return stack[-1]