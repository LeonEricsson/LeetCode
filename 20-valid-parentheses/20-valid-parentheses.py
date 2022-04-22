class Solution:
    def isValid(self, s: str) -> bool:
        left = "([{"
        right = ")]}"
        
        stack = []
        for c in s:
            if c in left:
                stack.append(right[left.index(c)])
            else:
                if not stack or c != stack.pop():
                    return False
        if stack:
            return False
        else: 
            return True