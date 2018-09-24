class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        lcp = ''

        for i in range(len(strs[0])):
            char = strs[0][i]
            all = True

            for s in strs:
                if i >= len(s) or s[i] != char:
                    all = False
                    break

            if all:
                lcp += char
            else:
                break

        return lcp
