# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        begin = ListNode("begin")
        tmp = begin

        while l1 is not None or l2 is not None:
            if l1 is None:
                begin.next = l2
                break
            elif l2 is None:
                begin.next = l1
                break
            elif l1.val < l2.val:
                begin.next = l1
                l1 = l1.next
                begin = begin.next
            else:
                begin.next = l2
                l2 = l2.next
                begin = begin.next

        return tmp.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            res = lists[0]
            for i in range(1,len(lists)):
                res = self.mergeTwoLists(res, lists[i])
            return res