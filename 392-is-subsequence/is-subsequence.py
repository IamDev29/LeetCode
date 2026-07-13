class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)>len(t):
            return False

        left=0
        right=0

        while left<len(s) and right<len(t):
            if s[left]==t[right]:
                left+=1
                right+=1
            else:
                right+=1

        if left!=len(s):
            return False
        else:
            return True