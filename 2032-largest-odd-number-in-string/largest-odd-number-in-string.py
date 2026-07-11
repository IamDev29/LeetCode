class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        ans=""

        for i in range(len(num)-1,-1,-1):
            digit=int(num[i])
            if digit%2!=0:
                return num[0:i+1]

        return ans
        