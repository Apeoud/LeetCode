class Solution(object):
    def get_candidate_times(self, candidates, target):
        res = dict()
        for e in candidates:
            if e in res.keys():
                res[e] += 1
            else:
                res.setdefault(e, 1)

        can, tim = [], []
        for key, value in res.items():
            if key <= target:
                can.append(key)
                tim.append(value)
        return can, tim

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if target == 0:
            return []

        candidates, times = self.get_candidate_times(candidates, target)
        if len(candidates) < 1:
            return []

        def get_combination(sets, tar):
            if len(sets) == 1:
                if int(tar / sets[0]) <= times[0]:
                    return [[sets[0]] * int(tar / sets[0])] if tar % sets[0] == 0 else []
                else:
                    return []
            else:
                res = []
                cur = 0
                while cur * sets[-1] <= tar and cur <= times[len(sets) - 1]:
                    tmp = get_combination(sets[:-1], tar - cur * sets[-1])
                    if len(tmp) > 0:
                        for t in tmp:
                            res.append(t + [sets[-1]] * cur)
                    cur += 1
                return res

        return get_combination(candidates, target)


if __name__ == "__main__":
    print(Solution().combinationSum2([2], 1))
