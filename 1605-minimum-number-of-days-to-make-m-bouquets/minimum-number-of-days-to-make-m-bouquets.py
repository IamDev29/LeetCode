class Solution(object):
    def possible(self,bloomDay,day,m,k):
        cnt=0
        noBloom=0

        for i in range(len(bloomDay)):
            if bloomDay[i]<=day:
                cnt+=1
            else:
                noBloom+=cnt//k
                cnt=0
                
        noBloom+=cnt//k

        if noBloom>=m:
            return True
        else:
            return False

    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if len(bloomDay)<m*k:
            return -1

        left=min(bloomDay)
        right=max(bloomDay)
        ans=right

        while left<=right:
            mid=(left+right)//2

            if self.possible(bloomDay,mid,m,k):
                ans=mid
                right=mid-1
            else:
                left=mid+1

        return ans

