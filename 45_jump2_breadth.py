import time


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return 0

        i = 1

        last_arrive = set()
        last_arrive.add(0)

        left = list(range(1, len(nums)))

        while True:
            cur_arrive = set()
            for ele in last_arrive:

                rem = list()
                for tmp in left:

                    if tmp <= ele + nums[ele]:
                        cur_arrive.add(tmp)
                        rem.append(tmp)

                        # cur_arrive.add(ele + 1 + step)

                        if tmp == len(nums) - 1:
                            return i

                    else:
                        break

                for ele in rem:
                    left.remove(ele)

            last_arrive = cur_arrive
            i += 1


if __name__ == "__main__":
    bt = time.time()
    sol = Solution()

    c = [1] * 100000
    print(sol.jump(c))

    et = time.time()

    print(et - bt)
