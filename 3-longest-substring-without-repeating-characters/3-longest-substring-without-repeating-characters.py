class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        usedChar = {}
        start = maxlength = 0
        
        for i, c in enumerate(s):
            if c in usedChar and start <= usedChar[c]:
                start = usedChar[c] + 1
            else:
                maxlength = max(maxlength, i - start + 1)
            usedChar[c] = i
        return maxlength
        