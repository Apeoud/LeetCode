"""
总结几种常用的排序算法
"""


def bubble_sort(nums):
    """
    冒泡排序，从后往前，依次把最小的放到前面
    :param nums:
    :return:
    """

    # TODO : python中list的赋值机制

    if not nums:
        return None

    for i in range(len(nums)):
        index = len(nums) - 1
        while index >= min(i, 1):
            if nums[index] < nums[index - 1]:
                nums[index - 1], nums[index] = nums[index], nums[index - 1]
            index -= 1

    return nums


def select_sort(nums):
    """
    选择排序，每次选择后面所有list中最小的进行交换
    :param nums:
    :return:
    """

    for i in range(len(nums) - 1):
        cur_min = i + 1
        for j in range(i, len(nums)):
            if nums[j] < nums[cur_min]:
                cur_min = j
        nums[i], nums[cur_min] = nums[cur_min], nums[i]
    return nums


def insert_sort(nums):
    """
    插入排序，从0开始，对每一个元素，依次选择合适的位置插入
    TODO:不够优雅 看看别人怎么写
    :param nums:
    :return:
    """

    for i in range(1, len(nums)):
        target = nums[i]

        j = i - 1

        while j >= 0:
            if nums[j] > target:
                nums[j + 1] = nums[j]
                j -= 1
            else:
                nums[j + 1] = target
                break
        if j == -1:
            nums[0] = target
    return nums


def quick_sort(nums):
    """
    快速排序，分治的思路，先根据一个基数将原始的列表分成两部分，然后递归的分别调用
    :param nums:
    :return:
    """

    def partition(nums, l, r):

        i, j = l, r
        pivot = nums[l]

        while i < j:
            while j > i and nums[j] > pivot:
                j -= 1

            while i < j and nums[i] <= pivot:
                i += 1

            if i == j:
                nums[i], nums[l] = nums[l], nums[i]
                partition(nums, l, i)
                partition(nums, i + 1, r)
            else:

                nums[i], nums[j] = nums[j], nums[i]

        return

    return partition(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    test1 = [23, 2, 43, 2, 13, 1, 432, 23, 32, 543, 465, 23, 54, 56, 28, 54]
    test2 = [5, 3, 8, 6, 4]

    # TODO : 多种test case

    quick_sort(test1)
    print(test1)
