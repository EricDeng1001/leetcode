from math import inf, floor, ceil

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)
        
        left = 0
        right = n
        lefted = False
        
        while 1:
            i = (left + right) // 2
            if n == 1:
                if lefted:
                    i = 1
                lefted = True
        
            j = (m + n + 1) // 2 - i
            
            leftMax = max(
                        nums2[i - 1] if i > 0 else -inf, 
                        nums1[j - 1] if j > 0 else -inf
                      )

            rightMin = min(
                        nums2[i] if i < n else inf,
                        nums1[j] if j < m else inf
                       )
            
            if leftMax <= rightMin:
                break
            else:
                if left == right:
                    break
                if nums1[j - 1] > nums2[i]:
                    left = i + 1
                else:
                    right = i - 1
        
        if (m + n) & 1:
            return leftMax
        else:
            return (rightMin + leftMax) / 2
        