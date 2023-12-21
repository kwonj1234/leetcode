class Solution:
    def isValid(self, s: str) -> bool:
        paren = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []

        for char in s:
            if char in paren.values():
                stack.append(char)
            elif char in paren:
                if not stack or stack.pop() != paren[char]:
                    return False
        if stack:
            return False
        return True
