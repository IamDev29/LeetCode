class Solution(object):
    def cap(self,wt,capacity):
        day=1
        load=0
        for i in range(len(wt)):
            if load+wt[i]>capacity:
                day+=1
                load=wt[i]
            else:
                load+=wt[i]
        return day
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        mx=max(weights)
        sm=sum(weights)

        while mx<=sm:
            capacity=(mx+sm)//2

            day=self.cap(weights,capacity)

            if day<=days:
                sm=capacity-1
            else:
                mx=capacity+1
        
        return mx

        