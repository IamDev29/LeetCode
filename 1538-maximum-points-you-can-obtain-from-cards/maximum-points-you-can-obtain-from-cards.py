class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        ans=0

        for i in range(k):
            ans+=cardPoints[i]

        rindex=len(cardPoints)-1
        lsum=ans
        rsum=0

        for i in range(k-1,-1,-1):
            lsum-=cardPoints[i]
            rsum+=cardPoints[rindex]
            ans=max(ans,lsum+rsum)
            rindex-=1

        return ans

        