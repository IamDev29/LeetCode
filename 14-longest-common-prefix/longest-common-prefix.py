class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        min_len = min(len(s) for s in strs)

        prefix=[]

        for i in range(min_len):
            ch=strs[0][i]
            for s in strs[1:]:
                if s[i]!=ch:
                    return "".join(prefix)

            prefix.append(ch)

        return "".join(prefix)




        