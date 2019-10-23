class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        direction_down = True
        line_counter = 0
        char_to_row = [0] * len(s)
        if numRows == 1:
            return s
        for pos in xrange(len(s)):
            char_to_row[pos] = line_counter
            if direction_down:
                line_counter += 1
            else:
                line_counter -=1
            if line_counter == numRows:
                direction_down = not direction_down
                line_counter = numRows - 2
            if line_counter == -1:
                direction_down = not direction_down
                line_counter = 1
        result_string = ''
        print char_to_row
        for row in xrange(numRows):
            for pos in xrange(len(s)):
                if char_to_row[pos] == row:
                    result_string += s[pos]
        return result_string


def main():
    s = Solution()
    print s.convert('AB', 3)
    print s.convert('AB', 3) == 'AB'
    print s.convert('ABC', 3)
    print s.convert('ABC', 3) == 'ABC'
    print s.convert('AB', 1)
    print s.convert('AB', 1) == 'AB'
    print s.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    print s.convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'

if __name__ == "__main__":
    main()