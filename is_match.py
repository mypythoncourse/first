class Solution(object):
    LEGAL_CHARS = "abcdefghijklmnopqrstuvwxyz"
    def is_one_empty_and_other_is_not(self, s, p):
        return (s == [] and p != []) or (p ==[] and s != [])

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        string_stack = list([char for char in s])
        pattern_stack = list([symbol for symbol in p])
        # self.is_one_empty_and_other_is_not(string_stack, pattern_stack)
        while pattern_stack and string_stack:
            symbol = pattern_stack.pop()
            char_at_task = string_stack[-1]
            if symbol == "*":
                match_symbol = pattern_stack[-1] if pattern_stack[-1] != '.' else char_at_task
                while (len(string_stack) !=0) and (string_stack[-1] == match_symbol):
                    last_symbol = string_stack.pop()
                string_stack += last_symbol
                pattern_stack.pop()
            elif symbol == ".":
                string_stack.pop()
            else:
                if char_at_task != symbol:
                    return False
            string_stack.pop()
        if string_stack and pattern_stack == []:
            return False
        if pattern_stack and string_stack == []:
            while pattern_stack != [] and pattern_stack[-1] == "*":
                pattern_stack.pop()
                pattern_stack.pop()
            if pattern_stack:
                return False
        return True



def main():
    s = Solution()
    print s.isMatch("", "") == True
    print s.isMatch("", "a") == False
    print s.isMatch("a", "") == False
    print s.isMatch("aa", "a") == False
    print s.isMatch("aa", "a*") == True
    print s.isMatch("ab", ".*") == True
    print s.isMatch("aab", "c*a*b") == True
    print s.isMatch("mississippi", "mis*is*p*.") == False
    
    
if __name__ == "__main__":
    main()