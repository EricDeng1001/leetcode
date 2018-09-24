class Solution: # O(lg10(x))
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # filter zero to make under filter work
        if x == 0:
            return True
        # filter neg and 10+ which make the alg not working
        if x < 0 or x % 10 == 0:
            return False
        
        reversed = 0
        
        while reversed < x:
            reversed *= 10
            reversed += x % 10
            x //= 10
        
        #  even case            odd case
        if reversed == x or reversed // 10 == x:
            return True
        return False
    
#Python solution O(n)
def isPalindrome(x):
    x = str(x)
    r = x[::-1]
    return r == s