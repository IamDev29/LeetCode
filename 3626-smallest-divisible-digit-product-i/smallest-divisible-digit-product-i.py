class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def digit_product(x):
            prod = 1
            while x > 0:
                prod *= x % 10
                x //= 10
            return prod

        x = n
        while True:
            if digit_product(x) % t == 0:
                return x
            x += 1
        