class Solution(object):
    def subset(self, sets):
        if len(sets) == 0:
            return []
        # 长度分别从1 到 len(sets)的子集
        res = []
        for i in range(1, 2 ** len(sets)):
            flag = list(bin(i).replace("0b", ""))
            flag.reverse()
            res.append([sets[k] for k in range(len(flag)) if flag[k] == '1'])

        return res

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if target == 0:
            return []

        candidates = [ele for ele in candidates if ele <= target]
        if len(candidates) < 1:
            return []
        times = [int(target / e) for e in candidates]

        def get_combination(sets, tar):
            if len(sets) == 1:
                return [[sets[0]] * int(tar / sets[0])] if tar % sets[0] == 0 else []
            else:
                res = []
                cur = 0
                while cur * sets[-1] <= tar and cur <= times[len(sets) - 1]:
                    tmp = get_combination(sets[:-1], tar - cur*sets[-1])
                    if len(tmp) > 0:
                        for t in tmp:
                            res.append(t+[sets[-1]] * cur)
                    cur += 1
                return res

        return get_combination(candidates, target)


if __name__ == "__main__":
    # print(Solution().subset([1, 2, 3]))
    print(Solution().combinationSum([2], 1))
