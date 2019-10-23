class Solution(object):
    DIGITS_TO_LETTERS = {}
    DIGITS_TO_LETTERS["2"] = "abc"
    DIGITS_TO_LETTERS["3"] = "def"
    DIGITS_TO_LETTERS["4"] = "ghi"
    DIGITS_TO_LETTERS["5"] = "jkl"
    DIGITS_TO_LETTERS["6"] = "mno"
    DIGITS_TO_LETTERS["7"] = "pqrs"
    DIGITS_TO_LETTERS["8"] = "tuv"
    DIGITS_TO_LETTERS["9"] = "wxyz"

    def helper(self, digit, result):
        if result == []:
            return [char for char in self.DIGITS_TO_LETTERS[digit]]
        else:
            new_result = []
            for char in self.DIGITS_TO_LETTERS[digit]:
                for part in result:
                    new_result.append(part + char)
            return new_result

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        for digit in digits:
            result = self.helper(digit, result)
        return result

if __name__ == "__main__":
    s = Solution()
    print s.letterCombinations("23")
