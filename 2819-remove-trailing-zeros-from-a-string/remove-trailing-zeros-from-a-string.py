class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        last=len(num)
        for i in range(len(num)-1,0,-1):
            if num[i]=='0':
                last-=1
            else:
                break

        return num[:last]