class Solution: # O(len(s) * len(p))
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # use i + 1 to allow i ahead of j, to check the tailed x*
        res = [[None for i in range(len(p))] for i in range(len(s) + 1)]

        def __isMatch(i, j):
            if j == len(p):
                return i == len(s)

            if res[i][j] is not None:
                return res[i][j]

            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if j < len(p) - 1 and p[j + 1] == '*':
                res[i][j] = match and __isMatch(i + 1, j) or __isMatch(i, j + 2)
                return res[i][j]

            res[i][j] = match and __isMatch(i + 1, j + 1)
            return res[i][j]

        return __isMatch(0, 0)
