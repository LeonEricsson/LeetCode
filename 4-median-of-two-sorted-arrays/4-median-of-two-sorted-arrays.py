class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        
        mid = ((n+m)/2)
                
        x = y = 0
        prev = cur = 0
        
        loops = mid + 1 if mid%1 == 0 else mid + 0.5
        
        
        for _ in range(int(loops)):
            prev = cur
            if x == n:
                cur = nums2[y]
                y += 1
            elif y == m:
                cur = nums1[x]
                x += 1
            elif nums1[x] <= nums2[y]:
                cur = nums1[x]
                x += 1
            else:
                cur = nums2[y]
                y += 1
        
        if mid % 1 == 0:
            return (prev+cur)/2
        else:
            return cur
