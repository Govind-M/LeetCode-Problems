class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        stack = []

        validmap = {
        '[':']',
        '{':'}',
        '(':')'
        } 

        for ch in s:
            if ch in validmap:
                stack.append(ch)
            elif len(stack)>0:
                top = stack.pop()
                if validmap[top] != ch:
                    return False
            else:
                return False
    
        return not stack
                    