class Solution(object):
    def isAdjacentDiffAtMostTwo(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s)-1):
            diff=abs(int(s[i])-int(s[i+1]))
            if diff>2:
                return False

        return True
        