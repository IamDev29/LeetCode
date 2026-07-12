class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        right=0

        ans=0

        for i in s:
            if i=='(':
                left+=1
            elif i==')':
                right+=1

            
            ans=max(ans,left-right)

        return ans


        