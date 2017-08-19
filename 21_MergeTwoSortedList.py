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


def printListNode(head):
    if head is None:
        print("None")
        return
    while head.next is not None:
        print(head.val)
        head = head.next
    print(head.val)


def create(NodeList):
    last = ListNode(NodeList[0])
    a = last
    for i in NodeList[1:]:
        tmp = ListNode(i)
        last.next = tmp
        last = tmp
    return a


if __name__ == "__main__":
    a = create([1])
    b = create([2])
    printListNode(a)
    printListNode(b)
    printListNode(Solution().mergeTwoLists(a,b))
