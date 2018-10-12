class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        saved = dict()

        def hash(s):

            return ''.join(sorted(s))

        for st in strs:
            hashed = hash(st)
            if hashed in saved.keys():
                saved[hashed].append(st)
            else:
                saved[hashed] = [st]

        return [v for k, v in saved.items()]
