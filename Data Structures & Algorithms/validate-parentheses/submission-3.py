class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chars = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in chars and stack:
                if stack[-1] != chars[char]: return False
                stack.pop()
            else: stack.append(char)
        
        return len(stack) == 0
