class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = maxArea = 0
        R = len(height) - 1
        
        while(L != R):            
            if(height[L] < height[R]):
                maxArea = max(maxArea, (R-L)*height[L])
                L += 1
            else:
                maxArea = max(maxArea, (R-L)*height[R])                
                R -= 1
        
        return maxArea