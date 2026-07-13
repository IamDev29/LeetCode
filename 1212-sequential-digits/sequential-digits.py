class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        s="123456789"
        ans=[]
        a=str(low)
        b=str(high)

        for length in range(len(a),len(b)+1):
            for start in range(0,10-length):
                num=int(s[start:start+length])

                if low<=num<=high:
                    ans.append(num)

        return ans