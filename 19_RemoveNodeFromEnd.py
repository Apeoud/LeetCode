# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        a = head
        nList = [head]
        length = 1
        while head.next is not None:
            length += 1
            nList.append(head.next)
            if len(nList) >= n + 1:
                nList = nList[len(nList) - n - 1:]
            head = head.next

        if n == length:
            return a.next
        if nList[0].next is not None:
            if nList[0].next.next is not None:
                nList[0].next = nList[0].next.next
            else:
                nList[0].next = None
            return a
        else:
            return None


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
    a = create([1,2])
    printListNode(a)
    printListNode(Solution().removeNthFromEnd(a, 2))
