class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=n**2
        b=n*(n+1)
        while a>0:
            b,a=a,b%a

        return b

