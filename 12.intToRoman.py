class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = convert4(num // 1000)
        num %= 1000
        roman += convert3(num // 100)
        num %= 100
        roman += convert2(num // 10)
        num %= 10
        roman += convert1(num)

        return roman

def convert1(num):
    if num == 0:
        return ''
    if num < 4:
        return "I" * num
    if num == 4:
        return "IV"
    if num < 9:
        return "V" + "I" * (num - 5)
    if num == 9:
        return "IX"

def convert2(num):
    if num == 0:
        return ''
    if num < 4:
        return "X" * num
    if num == 4:
        return "XL"
    if num < 9:
        return "L" + "X" * (num - 5)
    if num == 9:
        return "XC"

def convert3(num):
    if num == 0:
        return ''
    if num < 4:
        return "C" * num
    if num == 4:
        return "CD"
    if num < 9:
        return "D" + "C" * (num - 5)
    if num == 9:
        return "CM"

def convert4(num):
    if num == 0:
        return ''
    return "M" * num
