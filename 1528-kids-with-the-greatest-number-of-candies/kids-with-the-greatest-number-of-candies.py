class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxi=max(candies)
        ans=[]
        for i in candies:
            if i+extraCandies>=maxi:
                ans.append(True)
            else:
                ans.append(False)

        return ans
        