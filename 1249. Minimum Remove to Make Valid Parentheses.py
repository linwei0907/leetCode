class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            if char == ")":
                if not stack:
                    s[i] = ""
                else:
                    stack.pop()
        
        while stack:
            s[stack.pop()] = ""

        return "".join(s)
