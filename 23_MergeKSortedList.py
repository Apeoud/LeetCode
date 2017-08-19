# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def create(self, NodeList):
        if len(NodeList) == 0:
            return []
        last = ListNode(NodeList[0])
        a = last
        for i in NodeList[1:]:
            tmp = ListNode(i)
            last.next = tmp
            last = tmp
        return a

    def sortNodeList(self, sortList):
        return sorted(sortList, key=lambda x: x.val)

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        begin = ListNode("begin")
        tmp = begin

        val_dict = dict()
        for node in lists:
            while node is not None:
                if node.val in val_dict.keys():
                    val_dict[node.val] += 1
                else:
                    val_dict.setdefault(node.val, 1)
                node = node.next

        res = []
        for key, value in val_dict.items():
            res += [key] * int(value)

        return self.create(sorted(res))


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
    alist = [[0, 2, 5], [2, 3], [1, 2]]
    tmpList = []
    for a in alist:
        tmpList.append(create(a))
    print(type(tmpList))
    print(type(tmpList[0]))
    # printListNode(Solution().sortNodeList(tmpList))
    # printListNode(Solution().mergeKLists(tmpList))
