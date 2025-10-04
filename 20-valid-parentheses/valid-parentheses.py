class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        stack = []
        for c in s:
            if c in map:
                if stack and map[c]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if stack==[] else False