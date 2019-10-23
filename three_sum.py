class Solution(object):
    def threeSum(self, nums):
        result = {}
        nums.sort()
        n = len(nums)
        for i in xrange(n - 1):
            a = nums[i]
            start = i + 1
            end = n - 1
            while start < end:
                b = nums[start]
                c = nums[end]
                if a + b + c == 0:
                    result[(a, b, c)] = 1
                    start += 1
                    end -= 1
                elif a + b + c > 0:
                    end -= 1
                else:
                    start += 1
        return [list(key) for key in result.keys()]

def main():
    s = Solution()
    L = [-1, 0, 1, 2, -1, -4]
    result = [
        [-1, -1, 2],
        [-1, 0, 1]
    ]
    print s.threeSum(L) == result
    print s.threeSum(L)

if __name__ == "__main__":
    main()
