# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def size_of(self, l):
        length = 1
        while(l.next != None):
            length += 1
        return length

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        longer_list = l1 if self.size_of(l1) >= self.size_of(l2) else l2
        shorter_list = l1 if self.size_of(l1) < self.size_of(l2) else l2
        residual = 0
        final_result_list = ListNode(0)
        result_list = final_result_list
        for index in xrange(size_of(shorter_list)):
            curr_result = longer_list.val + shorter_list.val + residual
            result_list.val = curr_result % 10
            residual = curr_result / 10
            result_list.next = ListNode(0)
            result_list = result_list.next
            longer_list = longer_list.next
            shorter_list = shorter_list.next
        for index in xrange(size_of(longer_list) - size_of(shorter_list) + 1):
            curr_result = longer_list.val + residual
            result_list.val = curr_result % 10
            residual = curr_result / 10
            result_list.next = ListNode(0)
            result_list = result_list.next
            longer_list = longer_list.next
        return final_result_list
