class Solution(object):
    def __init__(self):
        ONE_SYMBOL_TO_VALUE = {}
        ONE_SYMBOL_TO_VALUE[1] = 'I'
        ONE_SYMBOL_TO_VALUE[5] = 'V'
        ONE_SYMBOL_TO_VALUE[10] = 'X'
        ONE_SYMBOL_TO_VALUE[50] = 'L'
        ONE_SYMBOL_TO_VALUE[100] = 'C'
        ONE_SYMBOL_TO_VALUE[500] = 'D'
        ONE_SYMBOL_TO_VALUE[1000] = 'M'
        temp = {ONE_SYMBOL_TO_VALUE[key]:key for key in ONE_SYMBOL_TO_VALUE.keys()}
        ONE_SYMBOL_TO_VALUE = temp
        TWO_SYMBOLS_TO_VALUE = {}
        TWO_SYMBOLS_TO_VALUE[4] = 'IV'
        TWO_SYMBOLS_TO_VALUE[9] = 'IX'
        TWO_SYMBOLS_TO_VALUE[40] = 'XL'
        TWO_SYMBOLS_TO_VALUE[90] = 'XC'
        TWO_SYMBOLS_TO_VALUE[400] = 'CD'
        TWO_SYMBOLS_TO_VALUE[900] = 'CM'
        temp = {TWO_SYMBOLS_TO_VALUE[key]:key for key in TWO_SYMBOLS_TO_VALUE.keys()}
        TWO_SYMBOLS_TO_VALUE = temp

    def get_next_num(self, s):
        if len(s) >= 2:
            for val in self.TWO_SYMBOLS_TO_VALUE.keys():
                if val == s[:2]:
                    return self.TWO_SYMBOLS_TO_VALUE[val], 2
        for val in self.ONE_SYMBOL_TO_VALUE.keys():
            if val == s[0]:
                return self.ONE_SYMBOL_TO_VALUE[val], 1

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        while len(s):
            value, how_much_to_trim = self.get_next_num(s)
            s = s[how_much_to_trim:]
            result += value
        return result

def main():
    s = Solution()
    print s.romanToInt("III") == 3
    print s.romanToInt("IV") == 4
    print s.romanToInt("IX") == 9
    print s.romanToInt("LVIII") == 58
    print s.romanToInt("MCMXCIV") == 1994


if __name__ == "__main__":
    main()
