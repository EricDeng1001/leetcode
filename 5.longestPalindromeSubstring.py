#apparoach expand around center

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_left = -1
        max_right = -1
        max_length = 0
        
        for i in range(2 * len(s) - 1):
            length = 0
            left = i // 2
            right = (i + 1) // 2
            
            while s[left - length] == s[right + length]:
                length += 1
                if left < length or right + length == len(s):
                    break
            
            if length + right - left > max_length:
                max_length = length
                max_left = left - length + 1
                max_right = right + length - 1
        
        return s[max_left: max_right + 1]
