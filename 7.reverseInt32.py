class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if x < 0:
            x = -x
            neg = True
        
        result = 0
        
        while x:
            last_digit = x % 10
            x //= 10
            result *= 10
            result += last_digit
        
        if neg:
            result = -result
        
        if result > 2147483647 or result < -2147483648:
            return 0
            
        return result