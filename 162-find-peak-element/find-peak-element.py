class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)

        if n==1:
            return 0

        low=0
        high=n-1

        peak=float('inf')

        while low<=high:
            mid=(low+high)//2

            if mid==0 and nums[mid+1]<nums[mid] or mid==n-1 and nums[mid-1]<nums[mid] or nums[mid-1]<nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid+1]>nums[mid]:
                low=mid+1
            else:
                high=mid-1