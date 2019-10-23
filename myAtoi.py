class Solution(object):
    NUMBERS = '0123456789'
    SIGNS = '+-'
    @staticmethod
    def is_empty_numnber(input_str):
        if len(input_str) == 0:
            return True
        return False

    @staticmethod
    def remove_spaces(input_str):
        return input_str.split(' ')

    @staticmethod
    def exists_non_empty_string_without_spaces(str_list):
        is_found = False
        for x in str_list:
            if x != '':
                is_found = True
        return is_found
    
    @staticmethod
    def get_first_non_empty_non_space_string(str_list):
        while str_list[0] == '': str_list = str_list[1:]
        return str_list[0]

    @staticmethod
    def is_signed_number(num_string):
        return num_string[0] in Solution.SIGNS and len(num_string) > 1 and num_string[1] in Solution.NUMBERS

    @staticmethod
    def is_negative(num_string):
        if not Solution.is_signed_number(num_string):
            return False
        if num_string[0] == "-":
            return True
        else:
            return False

    @staticmethod
    def is_start_with_legal_value(num_string):
        if num_string[0] in Solution.NUMBERS:
            return True
        if Solution.is_signed_number(num_string):
            return True
        return False

    @staticmethod
    def get_non_char_seperator(num_string):
        if Solution.is_signed_number(num_string):
            num_string = num_string[1:]
        for char in num_string:
            if char not in Solution.NUMBERS:
                return char

    @staticmethod
    def remove_seperator(num_string, seperator):
        return num_string.split(seperator)

    @staticmethod
    def valid_after_seperator(num_string_dots_seperated):
        if not Solution.all_legal_charachters(num_string_dots_seperated[0]):
            return False
        return True

    @staticmethod
    def get_seperator_separated_num_string(num_string_dots_seperated):
        return num_string_dots_seperated[0]

    @staticmethod
    def all_legal_charachters(num_string):
        if Solution.is_signed_number(num_string):
            num_string = num_string[1:]
        for char in num_string:
            if char not in Solution.NUMBERS:
                return False
        return True

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        if Solution.is_empty_numnber(str):
            return 0

        str_list =  Solution.remove_spaces(str)
        if not Solution.exists_non_empty_string_without_spaces(str_list):
            return 0

        num_string = Solution.get_first_non_empty_non_space_string(str_list)
        if not Solution.is_start_with_legal_value(num_string):
            return 0

        is_negative = False
        if Solution.is_signed_number(num_string):
            if Solution.is_negative(num_string):
                is_negative = True
                num_string = num_string[1:]

        non_char_seperator = Solution.get_non_char_seperator(num_string)
        num_string_dots_seperated = Solution.remove_seperator(num_string, non_char_seperator)
        if not Solution.valid_after_seperator(num_string_dots_seperated):
            return 0
        num_string = Solution.get_seperator_separated_num_string(
                        num_string_dots_seperated)

        if not Solution.all_legal_charachters(num_string):
            return 0
        if is_negative:
            num_string = '-{}'.format(num_string)
        if int(num_string) > 2**31 - 1:
            return 2**31 - 1
        if int(num_string) < -2**31:
            return -2**31
        return int(num_string)

def main():
    s = Solution()
    print s.myAtoi("") == 0
    print s.myAtoi(" ") == 0
    print s.myAtoi("-") == 0
    print s.myAtoi("1-0") == 1
    print s.myAtoi("-91283472332") == -2147483648
    print s.myAtoi("words and 987") == 0
    print s.myAtoi("4193 with words") == 4193
    print s.myAtoi("   -42") == -42
    print s.myAtoi("42") == 42
    print s.myAtoi("3.14") == 3
    print s.myAtoi('.1') == 0
    print s.myAtoi("  -0012a42") == -12
    print s.myAtoi("-5-") == -5

    
if __name__ == "__main__":
    main()
