class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=0

        minlen=float('inf')
        suma=0

        for right in range(len(nums)):
            suma+=nums[right]

            while suma>=target and left<=right:
                minlen=min(minlen,right-left+1)
                suma-=nums[left]
                left+=1
            

        if minlen==float('inf'):
            return 0
        else:
            return minlen