def binary_search(A, target):
    """
    二分法查找每个数值 原始的数字是升序的，可能存在重复的数字/没有重复的数字
    :param A:
    :param target:
    :return:
    """

    if len(A) == 0:
        return False

    if len(A) == 1:
        return target == A[0]

    begin = 0
    end = len(A) - 1

    while begin < end:
        mid = int((begin + end) / 2)

        if A[mid] == target:
            return mid

        elif target > A[mid]:
            begin = mid
        else:
            end = mid

    return False


if __name__ == "__main__":
    c = binary_search([1, 3, 6], 3)
    print(c)
