class Solution(object):
    def maxAreaWhenLargestIsToLeft(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        first_filler_index = [0] * len(height)
        max_area = 0
        for right_index in xrange(1, len(height)):
            for left_index in xrange(right_index - 1, -1, -1):
                if height[left_index] <= height[right_index]:
                    pass
        # for i, bin in enumerate(height):
        #     new_area = (i - first_taller_index[i]) * bin
        #     max_area = new_area if new_area > max_area else max_area
        # return max_area

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max1 = self.maxAreaWhenLargestIsToLeft(height)
        height.reverse()
        max2 = self.maxAreaWhenLargestIsToLeft(height)
        return max([max1, max2])

def main():
    s = Solution()
    L = [1,8,6,2,5,4,8,3,7]
    print s.maxArea(L) == 49
    print s.maxArea([1,2,1]) == 2
    
if __name__ == "__main__":
    main()
