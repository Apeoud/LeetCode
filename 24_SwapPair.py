# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        bef = ListNode("begin")
        tmp = bef
        if head is None:
            return None
        if head.next is None:
            return head
        while head is not None:
            if head.next is not None:
                bef.next = head.next
                head.next = head.next.next
                bef.next.next = head
                bef = head
                head = head.next
            else:
                break
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
    test = create([1, 2,3,4,5])

    printListNode(Solution().swapPairs(test))
