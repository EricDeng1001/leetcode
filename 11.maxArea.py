class Solution:
    def maxArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        return noDecreaseTraverse(heights)

def noDecreaseTraverse(heights): # O(n)
    """this alg scan through all combination that will not decrease the area.
    because max area must be formed by 0 <= i <= j <= len(heights) - 1,
    so we start from pair(0, len(heights) - 1), and move i, j toward the
    non-decreasing direction, this let us have an O(n) alg

    why it is faster than naive:
    it cut down many branches which will be smaller than counted max area
    """
    max_area, i, j = 0, 0, len(heights) - 1
    while i < j:
        max_area = max(max_area, min(heights[i], heights[j]) * (j - i))
        if heights[i] < heights[j]:
            i += 1 # if move j, it will be sure the area will be decreased
        else:
            j -= 1
    return max_area
