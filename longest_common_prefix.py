class Solution(object):
    def find_longesgt_match(self, str1, str2):
        longest_match = ""
        str1, str2 = (str1, str2) if len(str2) >= len(str1) else (str2, str1)
        for pos, char in enumerate(str1):
            if char != str2[pos]:
                return longest_match
            longest_match += char
        return longest_match

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not len(strs):
            return ""
        longest_common_prefix = strs[0]

        for string in strs:
            longest_common_prefix = self.find_longesgt_match(
                longest_common_prefix, string)
        return longest_common_prefix


def main():
    s = Solution()
    print s.longestCommonPrefix(["flower","flow","flight"]) == "fl"
    print s.longestCommonPrefix(["dog","racecar","car"]) == ""


if __name__ == "__main__":
    main()