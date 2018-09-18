class Solution:
    def myAtoi(self, s):
        """
        :type s: s
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0
        
        j = -1
        k = -1
        start = False
        neg = False
        count = 0
        for i in range(len(s)):
            char_code = ord(s[i])
            if char_code < ord('0') or char_code > ord('9'):
                if start:
                    break
                else:
                    if char_code == ord('+'):
                        count += 1
                    elif char_code == ord('-'):
                        count += 1
                        neg = not neg
                    else:
                        return 0
                    # logic required by the question: no more than one +-
                    if count > 1:
                        return 0
            else:
                if not start:
                    start = True
                    j = i
                k = i
        
        if j == -1: # only content symbols
            return 0
        
        result = int(s[j:k + 1]
        if neg:
            result = -result
        
        if result > 2147483647:
            return 2147483647
        if result < -2147483648:
            return -2147483648
        
        return result