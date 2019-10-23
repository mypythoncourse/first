class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        N = len(x_str)
        
        for pos in range(N):
            if x_str[pos] != x_str[N - 1 - pos]:
                return False
        return True
