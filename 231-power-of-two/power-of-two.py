class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        if n!=1 and n%2==1:
            return False

        while n>1:
            n=n//2

            if n!=1 and n%2==1:
                return False

        return True

        