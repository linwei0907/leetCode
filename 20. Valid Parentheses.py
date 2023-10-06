class Solution:
    def isValid(self, s: str) -> bool:
        open_par = {
            '(': 0,
            '[': 1,
            '{': 2
        }
        close_par = {
            ')': 0,
            ']': 1,
            '}': 2
        }

        result = []

        for char in s:
            if char in open_par:
                result.append(open_par[char])
            else:
                if not result or close_par[char] != result.pop():
                    return False
        
        if result:
            return False
        
        return True
