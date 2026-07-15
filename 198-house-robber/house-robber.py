class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        
        dp=[0]*(n+2)


        for i in range(n-1,-1,-1):
            take=nums[i]+dp[i+2]
            ntake=dp[i+1]

            dp[i]=max(take,ntake)

        return dp[0]
