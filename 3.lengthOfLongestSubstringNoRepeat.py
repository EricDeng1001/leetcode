class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = -1
        right = 0
        max_length = 0
        char_index = {}
        
        while right < len(s):
            char = s[right]
            if char in char_index:
                left = max(left, char_index[char])
            
            char_index[char] = right
            
            max_length = max(right - left, max_length)
                
            right += 1
        
        return max_length