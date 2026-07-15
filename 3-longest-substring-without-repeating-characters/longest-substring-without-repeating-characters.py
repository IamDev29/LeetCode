class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic={}

        if len(s)<=1:
            return len(s)

        left=0
        ans=0

        for i in range(len(s)):
            if s[i] in dic and dic[s[i]]>=left:
                ans=max(ans,i-left)
                left=dic[s[i]]+1
                dic[s[i]]=i
            else:
                dic[s[i]]=i
                ans=max(ans,i-left+1)

        return ans

        