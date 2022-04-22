class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        nrletter = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        ret = []
        self.dfs(digits, nrletter, "", ret)
        return ret
        
    
    def dfs(self, digits, nrletter, s, ret):
        if not digits:
            ret.append(s)
            return
        for c in nrletter[digits[0]]:  
            self.dfs(digits[1:], nrletter, s + c, ret)
        