class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        # P[i, j] = True iff s[i:j + 1] is a palidnrom 
        P = [[False for _ in s] for _ in s]
        substring = (0,0)
        for idx in xrange(len(s)):
            P[idx][idx] = True
            if idx != len(s) - 1:
                P[idx][idx + 1] = s[idx] == s[idx + 1]
                if P[idx][idx + 1]:
                    substring = (idx, idx + 1)

        for jump in xrange(2, len(s)):
            for start in xrange(len(s) - 1):
                stop = start + jump
                if stop >= len(s):
                    continue
                P[start][stop] = P[start + 1][stop - 1] and s[start] == s[stop]
                if P[start][stop] and stop - start + 1 > substring[1] - substring[0] + 1:
                    substring = (start, stop)
        return s[substring[0]: substring[1] + 1]



def main():
    s = Solution()
    print s.longestPalindrome('ababd')
    print s.longestPalindrome('cbbd')
    print s.longestPalindrome('a')
    print s.longestPalindrome('aaaax')
    print s.longestPalindrome('yaaaa')
    print s.longestPalindrome('aaaa')
    print s.longestPalindrome('')

if __name__ == "__main__":
    main()