class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low=1
        high=max(piles)
        ans=0

        while low<=high:
            mid=(low+high)//2
            

            time=0

            for item in piles:
                if item<=mid:
                    time+=1
                elif item%mid==0:
                    time+=item//mid
                else:
                    time+=(item//mid)+1

            if time<=h:
                high=mid-1
                ans=mid
            else:
                low=mid+1
                

        return ans
            