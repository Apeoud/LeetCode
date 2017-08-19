# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return self.val

    def __repr__(self):
        return str(self.val)


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """


        if head is None:
            return None

        last1 = ListNode("begin")
        last1.next = head
        tmo = last1

        while head is not None:
            group = head

            # 首先判断是不是还有k个node 如果有 进行reverse 否则 直接返回
            for i in range(k - 1):
                if head.next is not None:
                    head = head.next
                else:
                    return tmo.next
            line1 = group
            line2 = line1.next
            for i in range(k - 1):
                tmp = line2.next
                line2.next = line1
                line1 = line2
                line2 = tmp
            last1.next = line1
            last1 = group
            # 如果刚好结束 接k的整数倍个节点 那么直接返回即可 如果没有结束 先把当前k-group的1接到下一个group的1
            # 接续下一个轮回
            group.next = line2
            head = line2

        return tmo.next


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
    test = create([1])
    printListNode(Solution().reverseKGroup(test, 3))
