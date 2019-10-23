class Solution(object):
    VALUE_TO_SYMBOL = {}
    VALUE_TO_SYMBOL[1] = 'I'
    VALUE_TO_SYMBOL[5] = 'V'
    VALUE_TO_SYMBOL[10] = 'X'
    VALUE_TO_SYMBOL[50] = 'L'
    VALUE_TO_SYMBOL[100] = 'C'
    VALUE_TO_SYMBOL[500] = 'D'
    VALUE_TO_SYMBOL[1000] = 'M'
    VALUE_TO_SYMBOL[4] = 'IV'
    VALUE_TO_SYMBOL[9] = 'IX'
    VALUE_TO_SYMBOL[40] = 'XL'
    VALUE_TO_SYMBOL[90] = 'XC'
    VALUE_TO_SYMBOL[400] = 'CD'
    VALUE_TO_SYMBOL[900] = 'CM'
    VALUES = VALUE_TO_SYMBOL.keys()
    VALUES.sort(reverse=True)

    def get_num_to_subtract(self, num):
        for val in self.VALUES:
            if val <= num:
                return val

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        while num != 0:
            num_to_subtract = self.get_num_to_subtract(num)
            num -= num_to_subtract
            result += self.VALUE_TO_SYMBOL[num_to_subtract]
        return result


def main():
    s = Solution()
    print s.intToRoman(3) == "III"
    print s.intToRoman(4) == "IV"
    print s.intToRoman(9) == "IX"
    print s.intToRoman(58) == "LVIII"
    print s.intToRoman(1994) == "MCMXCIV"


if __name__ == "__main__":
    main()
