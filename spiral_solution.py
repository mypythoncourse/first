class Solution:
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        spiral = []
        left_boundary = 0
        right_boundary = len(A[0]) - 1
        up_boundary = 0
        down_boundary = len(A) - 1
        go_right_ptr = left_boundary
        go_down_ptr = up_boundary
        go_left_ptr = right_boundary
        go_up_ptr = down_boundary
        direction = Solution.RIGHT
        print up_boundary
        print down_boundary
        print up_boundary <= down_boundary 
        print left_boundary 
        print right_boundary
        print left_boundary <= right_boundary

        while up_boundary <= down_boundary and left_boundary <= right_boundary:
            print "direction = {dir}: spiral = {sp}".format(dir=direction, sp=spiral)
            if direction == Solution.RIGHT:
                go_right_ptr = left_boundary
                while go_right_ptr <= right_boundary:
                    spiral.append(A[up_boundary][go_right_ptr])
                    go_right_ptr += 1
                up_boundary += 1
            elif direction == Solution.DOWN:
                go_down_ptr = up_boundary
                while go_down_ptr <= down_boundary:
                    spiral.append(A[go_down_ptr][right_boundary])
                    go_down_ptr += 1
                right_boundary -= 1
            elif direction == Solution.LEFT:
                go_left_ptr = right_boundary
                while go_left_ptr >= left_boundary:
                    spiral.append(A[down_boundary][go_left_ptr])
                    go_left_ptr -= 1
                down_boundary -= 1
            elif direction == Solution.UP:
                go_up_ptr = down_boundary
                while go_up_ptr >= up_boundary:
                    spiral.append(A[go_up_ptr][left_boundary])
                    go_up_ptr -= 1
                left_boundary += 1
            direction = (direction + 1) % 4
        return spiral

    def maxset(self, A):
        max_sum = -1
        max_sum_sub_array = []
        candidat = []
        prev_len = 0
        for element in A:
            print candidat
            print max_sum_sub_array
            print "*" * 10
            if element < 0:
                if sum(candidat) > max_sum or (sum(candidat) == max_sum and prev_len < len(candidat)):
                    max_sum_sub_array = candidat
                    prev_len = len(candidat)
                    max_sum = sum(candidat)
                candidat = []
            else:
                candidat.append(element)
        if sum(candidat) > max_sum or (sum(candidat) == max_sum and prev_len < len(candidat)):
            max_sum_sub_array = candidat
        return max_sum_sub_array

    def coverPoints(self, A, B):
        # @param A : list of integers
        # @param B : list of integers
        # @return an integer
        total_num_of_steps = 0
        for idx1 in xrange(len(A) - 1):
            first_point = (A[idx1], B[idx1])
            second_point = (A[idx1 + 1], B[idx1 + 1])
            dp = [abs(x - y) for x, y in zip(first_point, second_point)]
            num_of_steps = min(dp) + max(dp) - min(dp)
            total_num_of_steps += num_of_steps
        return total_num_of_steps




