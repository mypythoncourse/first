class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if len(s) == 1:
            return x
        is_negative = s[0] == '-'
        s = s[1:] if is_negative else s
        out_s = ''.join([char for char in reversed(s)])
        while out_s[0] == '0': out_s = out_s[1:]
        out_s = '-{}'.format(out_s) if is_negative else out_s
        if int(out_s) > 2**32 - 1:
            return 0
        return int(out_s)


def main():
    s = Solution()
    print s.reverse(123) == 321
    print s.reverse(-123) == -321
    print s.reverse(120) == 21
    

if __name__ == "__main__":
    main()