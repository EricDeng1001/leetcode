class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        transform = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if not digits:
            return []

        if len(digits) == 1:
            return [x for x in transform[digits[0]]]

        def __leterCombinations(i):
            if i + 2 == len(digits):
                return [x + y
                    for x in transform[digits[i]]
                    for y in transform[digits[i + 1]]
                ]
            else:
                return [x + y
                    for x in transform[digits[i]]
                    for y in __leterCombinations(i + 1)
                ]

        return __leterCombinations(0)
