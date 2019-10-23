class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        closest_sum = sum(nums[0:3])
        for i in xrange(n - 1):
            a = nums[i]
            start = i + 1
            end = n - 1
            while start < end:
                b = nums[start]
                c = nums[end]
                res = a + b + c
                if abs(target - res) < abs(target - closest_sum):
                    closest_sum = res
                elif a + b + c > target:
                    end -= 1
                else:
                    start += 1
        return closest_sum

if __name__ == "__main__":
    L =  [-1, 2, 1, -4]
    target = 1
    s = Solution()
    print s.threeSumClosest(L, target) == 2
