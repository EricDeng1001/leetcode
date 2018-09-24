class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sym = {
            "I": 0,
            "V": 1,
            "X": 2,
            "L": 3,
            "C": 4,
            "D": 5,
            "M": 6
        }
        val = [1, 5, 10, 50, 100, 500, 1000]

        res = i = 0
        while i < len(s) - 1:
            if sym[s[i + 1]] - sym[s[i]] > 0: # IV IX XL
                res += val[sym[s[i + 1]]] - val[sym[s[i]]]
                i += 2
            else:
                res += val[sym[s[i]]]
                i += 1

        if i == len(s):
            return res
        return res + val[sym[s[len(s) - 1]]]
