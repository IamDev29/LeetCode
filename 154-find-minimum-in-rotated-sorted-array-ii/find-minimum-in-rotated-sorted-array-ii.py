class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low=0
        high=len(nums)-1
        ans=float('inf')

        while low<=high:
            mid=(low+high)//2

            ans=min(ans,nums[mid])
            if nums[low]==nums[mid]==nums[high]:
                low+=1
                high-=1
            elif nums[low]<=nums[mid]:
                ans=min(ans,nums[low])
                low=mid+1
            else:
                high=mid

        return ans