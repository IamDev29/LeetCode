class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt=0
        dic={}

        for ch in s:
            if ch not in dic:
                cnt+=1
                dic[ch]=1
            
        return cnt

        