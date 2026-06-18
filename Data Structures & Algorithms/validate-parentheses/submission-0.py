class Solution:
    def isValid(self, s: str) -> bool:
        foo = {'}':'{',
               ')':'(',
               ']':'['}
        stack = []
        for c in s:
            if c in foo:
                if len(stack) > 0  and foo[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0

        