import time


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def simple_match(s, p):
            all_index = []
            for i in range(len(s) - len(p) + 1):
                if s[i:i + len(p)] == p:
                    all_index.append(i)

            return all_index

        def match_rule(s, index, rule):

            if rule == "":
                return rule == s[:index]

            if "*" in rule:

                return len(s[:index]) >= rule.count("?")
            else:
                return len(s[:index]) == rule.count("?")

        # p_s = p.replace("*", "").replace("?", "")
        p_s = []

        # 第一个函数，把pattern重新组织成数组。用*来分割。
        # 两个规则：1.多个连续的*等于一个*
        # 2. 多个连续的字母串起来

        i = 0
        while i < len(p):

            if p[i] == "*":
                while i < len(p) and p[i] == "*":
                    i += 1
                p_s.append("*")

            elif p[i] == "?":
                p_s.append("?")
                i += 1

            else:
                char = []
                while i < len(p) and p[i] != "*" and p[i] != "?":
                    char.append(p[i])
                    i += 1

                p_s.append(''.join(char))

        # 第二步，对ps遍历，不断寻找符合条件的候选集合
        i = 0
        rule = [""]
        candidate = set()
        candidate.add(0)
        last_character = ""
        while i < len(p_s):
            if "?" not in p_s[i] and "*" not in p_s[i]:

                filtered = set()
                for candi in candidate:
                    candi_index = simple_match(s[candi+len(last_character):], p_s[i])
                    for index in candi_index:
                        if match_rule(s[candi+len(last_character):], index, ''.join(rule)):
                            filtered.add(candi + len(last_character) + index)
                candidate = filtered
                rule = [""]
                last_character = p_s[i]
            else:
                rule.append(p_s[i])

            i += 1

        filtered = set()
        for candi in candidate:

            if match_rule(s[candi+len(last_character):], len(s[candi+len(last_character):]), ''.join(rule)):
                filtered.add(candi)

        if len(filtered) >= 1:
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()

    bt = time.time()
    print(sol.isMatch(
        "aa",
        "*"))

    et = time.time()

    print(et - bt)
