class Solution(object):
    def isIsomorphic(self, s, t):
        dic_st = {}
        dic_ts = {}

        for i in range(len(s)):
            cs = s[i]
            ct = t[i]

            if cs in dic_st and dic_st[cs] != ct:
                return False
            if ct in dic_ts and dic_ts[ct] != cs:
                return False

            dic_st[cs] = ct
            dic_ts[ct] = cs

        return True