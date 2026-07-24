import math
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        left =1
        right=max(nums)
        
        while left<=right:
            mid=(left+right)//2
            sumi=0
            for num in nums:
                sumi+=math.ceil(float(num)/mid)

            if sumi<=threshold:
                right=mid-1
            else:
                left=mid+1

        return left