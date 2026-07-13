class Solution(object):
    def largestEven(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=""
        for i in range(len(s)-1,-1,-1):
            if int(s[i])%2==0:
                return s[0:i+1]
            
        return ans
        